'''
Write a python program than reads the csv file of the dataset and do tokenization and stemming.
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer as p_stem
from nltk.stem.snowball import SnowballStemmer as s_stem

file=open('file.csv','r')
content=file.read()
tokenize=word_tokenize(content)
print(tokenize)
print("\n")

answer=[p_stem().stem(tokenize) for tokenize in tokenize]
print(answer)
print("\n")

s_stem_englis=s_stem(language="english")
answer2=[s_stem_englis.stem(tokenize) for tokenize in tokenize]
print(answer2)
print("\n")