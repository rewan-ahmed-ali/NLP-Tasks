# #PorterStemmer
print("PorterStemmer")
print("==============================================================================")
# # ##1
'''
Write a program in Python that uses the NLTK library to implement the stemming process using the PorterStemmer algorithm.
'''
from nltk.stem.porter import PorterStemmer as p_stem
print(p_stem().stem("computer"))
print(p_stem().stem("dogs"))
print(p_stem().stem("traditional"))
print("==============================================================================")


# # ##2
'''
Write a program in Python that uses the NLTK library to perform stemming using the PorterStemmer algorithm on a list of words.
'''
from nltk.stem.porter import PorterStemmer as p_stem
text =['apes', 'bags',' computers', 'dogs', 'egos','frescoes','generous',
         'hats', 'igloos', 'jungles', 'kites', 'learners', 'mice', 
         'natives', 'openings', 'photos','queries', 'rats', 'scenes',
           'trees', 'utensils', 'veins', 'wells', 'xylophones', 'yoyos','zens']
answer =[p_stem().stem(text) for text in text]
print(answer)
# print(''.join(answer))
print("==============================================================================")


# #SnowballStemmer
print("SnowballStemmer")
print("==============================================================================")
# ##1
'''
Use the NLTK library to print the list of languages supported by SnowballStemmer.
'''
from nltk.stem.snowball import SnowballStemmer as s_stem
print(s_stem.languages)
print("==============================================================================")

'''
Write a program in Python that uses the NLTK library to perform stemming using the SnowballStemmer algorithm on a list of words.
'''
# ##2
from nltk.stem.snowball import SnowballStemmer as s_stem
s_stem_ENG = s_stem(language="english")
text2 = ['apes', 'bags', 'computers', 'dogs', 'egos', 'frescoes', 'generous',
         'hats', 'igloos', 'jungles', 'kites', 'learners', 'mice',
         'natives', 'openings', 'photos', 'queries', 'rats', 'scenes',
         'trees', 'utensils', 'veins', 'wells', 'xylophones', 'yoyos', 'zens']
answer2 = [s_stem_ENG.stem(text2) for text2 in text2]
print(answer2)
# print(' '.join(answer2))
print("==============================================================================")