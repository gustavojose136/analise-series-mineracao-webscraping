from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def example_similarity(docs):
    vectorizer = TfidfVectorizer(stop_words='portuguese')
    tfidf = vectorizer.fit_transform(docs)
    return cosine_similarity(tfidf)
