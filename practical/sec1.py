from nltk.tokenize import sent_tokenize , word_tokenize
text="I traveled to Los Anglos. I visited many places"
print(text.split())
# nltk tokenize sentence
print(sent_tokenize(text))
# nltk tokenize words
print(word_tokenize(text))


text2="Jane lent $100 to Peter early this morning."
# nltk tokenize words
content=word_tokenize(text2)
print(content)
#using split function
content_split=text2.split()
print(content_split)

text1 = "NLTK is a leading platform for building Python programs to work with human language data. It provides easy to use interf aces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming , t agging, parsing, and semantic reasoning, wrappers for industrial strength NLP libraries, and an active discussion forum."
# nltk tokenize sentence
sentence=sent_tokenize(text1)
print(sentence)