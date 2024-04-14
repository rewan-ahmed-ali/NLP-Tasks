import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# (Stop words) =>"the", "is", "and"
text = "Spacy is designed specifically for production use and build NLP applications to process large volumes of text different from NLTK focused on teaching and learning perspective."
# text = input("Enter the text: ")
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
filtered_text = ' '.join(filtered_tokens)
print("Filtered Text:")
print(filtered_text)
