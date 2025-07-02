from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def example_keywords(docs, top_n=5):
    vectorizer = CountVectorizer(stop_words='portuguese')
    X = vectorizer.fit_transform(docs)
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=[f"doc{i+1}" for i in range(len(docs))]).T
    top_terms = {}
    for doc in df.columns:
        top_terms[doc] = df[doc].sort_values(ascending=False).head(top_n).index.tolist()
    return top_terms
