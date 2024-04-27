"""
Question (1):
Write a python program that take an input text from the user and tokenize the text itnto sentences using languages
other than English using spacy library.
"""
import spacy
text = input("Enter the text in french: ") #Le chat mange la souris. Le chien court dans le jardin. Les oiseaux chantent dans les arbres.
language_code = input("Enter the language code (e.g., 'fr' for French, 'de' for German): ")
language_model_name = f"{language_code}_core_news_sm"
nlp = spacy.load(language_model_name)

# Tokenize sentences
text_doc = nlp(text)
sentences = [sentence.text for sentence in text_doc.sents]
print("Tokenized Sentences:\n")
for sentence in sentences:
    print(sentence)

# Tokenize words
words = [token.text for token in text_doc if not token.is_space]

print("\nTokenized Words:\n")
print(words)

