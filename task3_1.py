# Question (1):
#Le chat mange la souris. Le chien court dans le jardin. Les oiseaux chantent dans les arbres.
#القطة تأكل الفأر. الكلب يركض في الحديقة. الطيور تغني في الأشجار.
import spacy
text = input("Enter the text: ")
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

