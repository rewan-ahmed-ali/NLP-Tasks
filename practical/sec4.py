#1
import spacy
# Load the English language model
nlp=spacy.load("en_core_web_sm")
text = "Spacy is designed specifically for production use and build NLP applications to process large volumes of text different from NLTK focused on teaching and learning perspective. Tokenization is the process of breaking down text into individual words or tokens."
#It will convert any text string object into a nlp object.
text_doc=nlp(text)
print(text_doc)
#Convert Text Document Into Sentence Object
text_sent=[token.text for token in text_doc.sents]
print("sentence tokenize : ",text_sent)
#Directly Tokenize Text Document
tokenize=[token.text for token in text_doc]
print("word tokenize : ",tokenize)
print("==============================================================================")
print(len(text))


#2
'''nltk tokenization vs spacy tokenization'''
text = "Spacy is designed specifically for production use and build NLP applications to process large volumes of text different from NLTK focused on teaching and learning perspective. Tokenization is the process of breaking down text into individual words or tokens."
#nltk tokenization
from nltk.tokenize import word_tokenize
tokenize1=word_tokenize(text)
print(tokenize1)
print("==============================================================================")
#spacy tokenization
import spacy
nlp=spacy.load("en_core_web_sm")
text_doc=nlp(text)
tokenize11=[token.text for token in text_doc]
print(tokenize11)
print("==============================================================================")
#3
'''Exercise Given an input text, removing stop words from a text using NLTK library.'''
# (Stop words) =>"the", "is", "and"
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "Spacy is designed specifically for production use and build NLP applications to process large volumes of text different from NLTK focused on teaching and learning perspective."
# text = input("Enter the text: ")
tokenize12 = word_tokenize(text)
print(tokenize12)
print("==============================================================================")
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokenize12 if word.lower() not in stop_words]
print(filtered_tokens)
print("==============================================================================")
# filtered_text = ' '.join(filtered_tokens)
# print("Filtered Text:")
# print(filtered_text)
