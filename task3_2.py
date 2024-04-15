# Question (2):
# Write a python program that take an input text from the user and apply part-of-speech tagging, and return back correct tags per word.
# Note: use two different tagset and compare the output.
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
    
    # print("\nTagged words with Universal POS Tagset:")
    tagged_words_universal = pos_tagging_universal(input_text)
    # for token, tag in tagged_words_universal:
    #     print(f"{token}: {tag}")
        
    # print("\n------------------------------------------------------")
    # print("\nTagged words with default POS Tagging:")
    tagged_words_default = pos_tagging_default(input_text)
    # for word, tag in tagged_words_default:
    #     print(f"{word}: {tag}")

    print("\nComparison:")
    print("-----------------------------------------------------------------------")
    print("{:<20} {:<30} {:<20}".format("Word (sentence)", "Tag (Universal)", "Tag( default)"))
    print("-----------------------------------------------------------------------")
    for (token_universal, tag_universal), (token_default, tag_default) in zip(tagged_words_universal, tagged_words_default):
        print("{:<20} {:<30} {:<20}".format(token_universal, tag_universal, tag_default))

#  For example:
# - In the Universal POS Tagset, "went" is tagged as VERB, while in the default tagging, it's tagged as VBD (Past tense verb).
# - Similarly, "He" is tagged as PRON in the Universal tagset, whereas it's tagged as PRP (Personal Pronoun) in the default tagging.

# These differences arise because the Universal POS Tagset aims for simplicity and language independence,
#  while the default tagging in NLTK is more detailed and tailored specifically for English.