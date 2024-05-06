import nltk
from nltk.corpus import stopwords

def get_stopwords(language):
    nltk.download('stopwords')
    return set(stopwords.words(language))

if __name__ == "__main__":
    languages = ['english', 'spanish', 'french', 'german', 'italian', 'dutch', 'portuguese', 'russian', 'arabic', 'swedish']
    
    for lang in languages:
        stop_words = get_stopwords(lang)
        print(f"\nStop words in {lang.capitalize()}:\n{stop_words}")
