from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def example_tfidf(docs):
    vectorizer = TfidfVectorizer(stop_words='portuguese')
    tfidf_matrix = vectorizer.fit_transform(docs)
    df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=[f"doc{i+1}" for i in range(len(docs))]).T
    return df
