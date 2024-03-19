import csv
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer, PorterStemmer

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])  
    return data

def tokenize(text):
    tokens = word_tokenize(text)
    return tokens

def snowball_stem(tokens):
    stemmer = SnowballStemmer(language='english')
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def porter_stem(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def main():
    file_path = 'Emotion_classify_Data.csv'
    data = read_csv_file(file_path)

    for text in data:
        tokens = tokenize(text)
        snowball_stemmed_tokens = snowball_stem(tokens)
        porter_stemmed_tokens = porter_stem(tokens)
        print("Original Text:", text)
        print("Tokenized Text:", tokens)
        print("Snowball Stemmed Text:", snowball_stemmed_tokens)
        print("Porter Stemmed Text:", porter_stemmed_tokens)
        print("=" * 50)


if __name__ == "__main__":
    main()
