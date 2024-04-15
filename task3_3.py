# Question (3):
# Write a Python NLTK program to get a list of common stop words in various languages in Python.
import nltk
from nltk.corpus import stopwords

def common_stopwords_languages():
    languages = stopwords.fileids()
    common_stopwords = {}
    for lang in languages:
        stopwords_list = stopwords.words(lang)
        common_stopwords[lang] = stopwords_list
    return common_stopwords

if __name__ == "__main__":
    common_stopwords = common_stopwords_languages()
    for lang, stopwords_list in common_stopwords.items():
        print(f"Common Stopwords in {lang}: {stopwords_list[:10]}")
