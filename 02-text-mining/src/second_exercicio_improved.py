import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from spacy.cli import download as spacy_download
from collections import Counter
import matplotlib.pyplot as plt

# Download de recursos
nltk.download('stopwords')
try:
    nlp = spacy.load('pt_core_news_sm')
except OSError:
    spacy_download('pt_core_news_sm')
    nlp = spacy.load('pt_core_news_sm')

# Carrega dataset
df = pd.read_csv('../data/comments_dataset_pt_improved.csv')

# Stop-words PT
stopwords_pt = stopwords.words('portuguese')

# 1. Term Frequency Analysis (Keyword Analysis: top 10 termos)
cv = CountVectorizer(stop_words=stopwords_pt)
dtm = cv.fit_transform(df['comentario'])
freq = dtm.sum(axis=0).A1
terms = cv.get_feature_names_out()
top10 = sorted(zip(terms, freq), key=lambda x: x[1], reverse=True)[:10]
print('Top 10 termos mais frequentes:', top10)

# 2. TF-IDF
tfidf_vec = TfidfVectorizer(stop_words=stopwords_pt)
tfidf = tfidf_vec.fit_transform(df['comentario'])
df_tfidf = pd.DataFrame(tfidf.toarray(), columns=tfidf_vec.get_feature_names_out())
print('\nTop 5 TF-IDF no comentário 1:', df_tfidf.iloc[0].sort_values(ascending=False).head(5))

# 3. Sentiment Analysis (léxico simples)
positivos = set(['ótimo','excelente','adorei','incrível','sensacional','útil','top','fantástico','perfeito'])
negativos = set(['ruim','péssimo','problema','lento','difícil','insuportável','chato'])
def pontuar(texto):
    tokens = texto.lower().split()
    return sum(t in positivos for t in tokens) - sum(t in negativos for t in tokens)
df['sentiment_score'] = df['comentario'].apply(pontuar)
print('\nSentiment scores 10 primeiros:\n', df[['comentario','sentiment_score']].head(10))

# 4. Topic Modeling (LDA)
lda = LatentDirichletAllocation(n_components=2, random_state=0)
lda.fit(dtm)
print('\nTópicos LDA:')
for i, comp in enumerate(lda.components_):
    terms_i = [terms[idx] for idx in comp.argsort()[-5:]]
    print(f'Tópico {i+1}:', terms_i)

# 5. Text Similarity (cosine entre 1º e 2º comentário)
sim = cosine_similarity(tfidf[0], tfidf[1])[0][0]
print(f'\nSimilaridade coseno entre 1º e 2º comentário: {sim:.2f}')

# 6. Named Entity Recognition
print('\nEntidades nomeadas (5 primeiros comentários):')
for doc in nlp.pipe(df['comentario'].head(5)):
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    print(ents)

# 7. Coding Qualitative Data (categorias simples)
def categorizar(texto):
    txt = texto.lower()
    if 'tutorial' in txt or 'dica' in txt: return 'Dicas'
    if 'tutorial' not in txt and 'ótimo' in txt: return 'Elogio'
    return 'Outro'
df['categoria'] = df['comentario'].apply(categorizar)
print('\nCategorias:', df['categoria'].value_counts().to_dict())

# 8. Visualizing Text Data (Word Cloud e gráfico de barras)
# Gráfico de barras Top10 termos
freq_series = pd.Series(dict(top10))
plt.figure(figsize=(8,4))
freq_series.sort_values().plot.barh()
plt.title('Top 10 termos frequentes')
plt.tight_layout()
plt.savefig('bar_top10.png')

from wordcloud import WordCloud
wc = WordCloud(width=400, height=200, stopwords=set(stopwords_pt))
wc.generate(' '.join(df['comentario']))
wc.to_file('wordcloud.png')
print('\nGráficos salvos: bar_top10.png e wordcloud.png')
