from wordcloud import WordCloud
import matplotlib.pyplot as plt

def example_wordcloud(text, **kwargs):
    wc = WordCloud(width=800, height=400, **kwargs).generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
