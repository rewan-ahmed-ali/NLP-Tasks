import nltk
def tokenize_words(text):
    return nltk.word_tokenize(text)

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

def main():
    text = input("Enter some text: ")
    choice = input("Choose one of the following options:\n"
                   "1. Print tokenized words\n"
                   "2. Print tokenized sentences\n"
                   "3. Print output using split function\n"
                   "Enter your choice (1/2/3): ")

    if choice == '1':
        tokens = tokenize_words(text)
        # print(tokens)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.chunk.ne_chunk(tagged)
        words = []
        for entity in entities:
            if isinstance(entity, nltk.Tree):
                entity_name = ' '.join([word for word, tag in entity.leaves()])
                words.append(entity_name)
            else:
                words.append(entity[0])
        final_tokens = []
        for word in words:
            if ' ' in word:
                final_tokens.append(word)
            else:
                final_tokens.extend(tokenize_words(word))
        print("Tokenized words:\n",final_tokens)

    elif choice == '2':
        sentences = tokenize_sentences(text)
        print("Tokenized sentences:\n",sentences)
        for idx, sentence in enumerate(sentences, start=1):
            print(f"Sentence {idx}: {sentence}")
    elif choice == '3':
        words = text.split()
        print("Output using split function:\n", words)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()