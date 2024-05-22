'''
Question (1):
Write a python program that take an input text from the user and tokenize the text itnto sentences using languages
other than English using spacy library.
'''
import spacy
# text=input("Enter sentence:")
text="Le chat mange la souris. Le chien court dans le jardin. Les oiseaux chantent dans les arbres."
nlp=spacy.load("fr_core_news_sm")
text_doc=nlp(text)
print(text_doc)
tokenize1=[token.text for token in text_doc]
print("\ntokenize word=>",tokenize1)
tokenize2=[token.text for token in text_doc.sents]
print("\ntokenize sentence=>",tokenize2)

'''
Question (2):
Write a python program that take an input text from the user and apply part-of-speech tagging, 
and return back correct tags per word.
Note: use two different tagset and compare the output.
'''
from nltk.tokenize import word_tokenize 
from nltk import pos_tag 
text="Call Me Later"
# text=input("Enter Text:")
tokenize=word_tokenize(text)
pos_tagg1=pos_tag(tokenize,tagset='universal')
print("Tagged words with Universal POS tags:",pos_tagg1)
pos_tagg2=pos_tag(tokenize)
print("Tagged words with Penn Treebank POS tags:",pos_tagg2)


'''
Question (3): Write a Python NLTK program to get a list of common stop words in various languages in Python.
'''
from nltk.corpus import stopwords
stopwords_english = stopwords.words('english')
print(stopwords_english)
print('\n')
stopwords_french = stopwords.words('french')
print(stopwords_french)
print('\n')
stopwords_arabic = stopwords.words('arabic')
print(stopwords_arabic)