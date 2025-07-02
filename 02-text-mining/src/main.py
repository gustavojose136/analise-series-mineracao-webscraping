import nltk
nltk.download('stopwords')

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords

# Carrega dataset
df = pd.read_csv('../data/comments_dataset_pt.csv')

# Carrega stop-words em português
stopwords_pt = stopwords.words('portuguese')

# Exemplo 1: TF-IDF com stop-words PT
vectorizer = TfidfVectorizer(stop_words=stopwords_pt)
tfidf_matrix = vectorizer.fit_transform(df['comentario'])
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print("Top 5 termos TF-IDF do comentário 1:")
print(df_tfidf.iloc[0].sort_values(ascending=False).head(5))

# Exemplo 2: Análise de Sentimento
positivos = {"ótimo", "excelente", "adorei", "incrível", "sensacional", "útil", "top", "fantástico", "perfeito"}
negativos = {"ruim", "péssimo", "problema", "lento", "difícil", "insuportável", "chato"}

def pontuar_sentimento(texto):
    tokens = texto.lower().split()
    pos = sum(1 for t in tokens if t in positivos)
    neg = sum(1 for t in tokens if t in negativos)
    return pos - neg

df['sentiment_score'] = df['comentario'].apply(pontuar_sentimento)
print("\nSentiment scores dos 10 primeiros comentários:")
print(df[['comentario', 'sentiment_score']].head(10))

# Exemplo 3: Modelagem de Tópicos com LDA
cv = CountVectorizer(stop_words=stopwords_pt)
dtm = cv.fit_transform(df['comentario'])
lda = LatentDirichletAllocation(n_components=2, random_state=0)
lda.fit(dtm)
print("\nTópicos LDA:")
for idx, comp in enumerate(lda.components_):
    termos = [cv.get_feature_names_out()[i] for i in comp.argsort()[-5:]]
    print(f"Tópico {idx+1}: {', '.join(termos)}")
