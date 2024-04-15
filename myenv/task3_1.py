#write myenv\Scripts\activate in terminal
# Question (1):
# Write a python program that take an input text from the user and tokenize the text itnto sentences using languages other than English using spacy library.
import spacy
text = input("Enter the text: ")
#Le chat mange la souris. Le chien court dans le jardin. Les oiseaux chantent dans les arbres.
#القطة تأكل الفأر. الكلب يركض في الحديقة. الطيور تغني في الأشجار.
# Load the language model for the desired language
language_code = input("Enter the language code (e.g., 'fr' for French, 'de' for German): ")
language_model_name = f"{language_code}_core_news_sm"
nlp = spacy.load(language_model_name)

# Tokenize the text into sentences
text_doc = nlp(text)
sentences = [sentence.text for sentence in text_doc.sents]

# Print the tokenized sentences
print("Tokenized Sentences:")
for sentence in sentences:
    print(sentence)
