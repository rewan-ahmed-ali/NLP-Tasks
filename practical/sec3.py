'''
Write a Python program that uses the NLTK library to generate 2-grams from the given sentence below.
text ="The cow jumps over the moon."
'''
#1
from nltk import ngrams
sentence="The cow jumps over the moon."
NGRAM=ngrams(sentence.split(),n=2)
for grams in NGRAM:
    print(grams)
print("==============================================================================")

'''
Write a program in Python that uses the NLTK library to generate n-grams input text from the user
'''
#2
import nltk 
from nltk import ngrams
sentence=input("Enter sentence:")
n=int(input("Enter value of (N):"))
N_GRAMS=ngrams(sentence.split(),n)
for grams in N_GRAMS:
    print(grams)