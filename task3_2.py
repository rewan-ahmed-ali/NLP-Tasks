# Question (2):
import nltk
from nltk.tokenize import word_tokenize
#sentence=>Spacy is designed specifically for production use and build NLP applications to process large volumes of text different from NLTK focused on teaching and learning perspective
def pos_tagging_universal(input_text):
    tokens = word_tokenize(input_text)
    tagged_words = nltk.pos_tag(tokens, tagset='universal')
    return tagged_words

def pos_tagging_default(input_text):
    tokens = nltk.word_tokenize(input_text)
    tagged_words = nltk.pos_tag(tokens)
    # tagged_words = nltk.pos_tag(tokens, tagset='treebank')
    return tagged_words

if __name__ == "__main__":
    input_text = input("Enter a sentence: ")
    tagged_words_universal = pos_tagging_universal(input_text)
    tagged_words_default = pos_tagging_default(input_text)
    
    print("\nComparison:")
    print("-----------------------------------------------------------------------")
    print("{:<20} {:<30} {:<20}".format("Word (sentence)", "Tag (Universal)", "Tag( default)"))
    print("-----------------------------------------------------------------------")
    for (token_universal, tag_universal), (token_default, tag_default) in zip(tagged_words_universal, tagged_words_default):
        print("{:<20} {:<30} {:<20}".format(token_universal, tag_universal, tag_default))

