'''
1- Write a python program than takes a text from a user and ask the user to choose one of three choices:
Choice number 1: print tokenized words
Choice number 2: print tokenized sentences
Choice number 3: print output using split function.
'''
from nltk.tokenize import word_tokenize, sent_tokenize
text = input("Enter text : \n")
choice = int(input("Choose method:\n1-word tokenization\n2-sentence tokenization\n3-split function\nEnter number of your choice: "))

if choice==1:
    print(word_tokenize(text))
elif choice ==2:
    print(sent_tokenize(text))
elif choice ==3:
    print(text.split())
else:
    print('Please enter a choice [1-3]:')