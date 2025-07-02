from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def example_lda(docs, n_topics=2, n_top=5):
    cv = CountVectorizer(stop_words='portuguese')
    X = cv.fit_transform(docs)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    lda.fit(X)
    terms = cv.get_feature_names_out()
    topics = {}
    for i, comp in enumerate(lda.components_):
        top_idx = comp.argsort()[-n_top:][::-1]
        topics[f'Topic{i+1}'] = [terms[j] for j in top_idx]
    return topics
