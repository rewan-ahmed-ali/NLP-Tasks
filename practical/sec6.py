'''
Use spaCy to load the en_core_web_md model,
process the sentence "i ate a banana", 
and print the vector for the word "banana".
'''

import spacy
nlp = spacy.load("en_core_web_md")
text = "i ate a banana"
text_doc = nlp(text)
banana_vector = text_doc[3].vector  # كلمة "banana" في الفهرس 3
print(banana_vector)

import en_core_web_md
nlp=en_core_web_md.load()
text="i ate a banana"
text_doc=nlp(text)
word_vectors=text_doc[3].vector
print(word_vectors)
