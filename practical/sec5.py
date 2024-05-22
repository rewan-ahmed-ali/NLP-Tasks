#1
# This will print the first 40 tagged words from the Brown Corpus.
from nltk.corpus import brown
print(brown.tagged_words()[:40])

#2
# how to tokenize sentences to words and perform POS tagging using NLTK
from nltk.tokenize import word_tokenize 
from nltk import pos_tag 
text1="Give me a call"
utt1 = word_tokenize(text1)
tagged_tokens1 =pos_tag(utt1, tagset='universal')
print(tagged_tokens1)

text2="Call me later"
tokenize2 = word_tokenize(text2)
tagged_tokens2=pos_tag(tokenize2, tagset='universal')
print(tagged_tokens2)

#3
#nltk classifier
from nltk.tokenize import word_tokenize 
from nltk import pos_tag ,ne_chunk
text1="Give me a call"
tokenize1 = word_tokenize(text1)
tagged_tokens1 =pos_tag(tokenize1, tagset='universal')
print(tagged_tokens1)
ner_tree1 = ne_chunk(tagged_tokens1)
print("Named entities in tokenize1:", ner_tree1)

text2="Call me later"
tokenize2 = word_tokenize(text2)
tagged_tokens2=pos_tag(tokenize2, tagset='universal')
print(tagged_tokens2)
ner_tree2 = ne_chunk(tagged_tokens2)
print("Named entities in tokenize2:", ner_tree2)


# # Import word_tokenize and pos_tag as w_tok and p_tag
# from nltk.tokenize import word_tokenize as w_tok 
# from nltk import pos_tag as p_tag
# #Create and tokenizer two sample utterances utt1 and utt2
# utt1 = w_tok("Give me a call")
# utt2 = w_tok("Call me later")
# print(p_tag(utt1, tagset='universal'))
# print(p_tag(utt2, tagset='universal'))