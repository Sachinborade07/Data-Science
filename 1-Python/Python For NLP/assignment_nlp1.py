#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 01:03:32 2024

@author: Sachin Borade
"""
# Assignment (Take the review from flipcard and perform all the operation
#  till now)

flipcard_godrej = '''
I ordered godrej 180 l direct cool single door 2 star refrigerator in May 29th 
order received may 30 after 5 days use i write this review this godrej 
refrigerator is enough for 2 or 3 people small family and bachelor cooling 
effect is good freezing ice cubes with in a 3 hours only disappoint i expect 
the class shelf but in this model have grill shelf but disign is okay this
 price over all good 
'''

# 1. Performing Tokenization 

import nltk 
from nltk import word_tokenize
words = word_tokenize(flipcard_godrej)
print(words)

# 2. Removing StopWords 

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

tokens = [word for word in words if word.lower() not in stop_words]
print(tokens)

# 3. Auto correcting the words 
from autocorrect import Speller

# Creating an object 
spell = Speller(lang='en')

#list comprehension 
corrected_words = [spell(word) for word in tokens]
print(corrected_words)

# 4. Performing the Stemming operation on it 
import nltk 

#creating an object 
stemmer = nltk.stem.PorterStemmer()
corrected_words = [stemmer.stem(word) for word in corrected_words]
print(corrected_words)


# 5. The sentence now is 
sentence = " ".join([spell(word) for word in corrected_words])
print(sentence)

##############################################################################

# Performing the Regular Expression of the above text data 
flipcard_godrej = '''
I ordered godrej 180 l direct cool single door 2 star refrigerator order May 29th 
 received may 30 after 5 days use i write this review this godrej 
refrigerator is enough for 2 or 3 people small family and bachelor cooling 
effect is good freezing ice cubes with in a 3 hours only disappoint i expect 
the class shelf but in this model have grill shelf but disign is okay this
 price over all good 
'''

# Extracting order date by pattern matching 
import re
pattern = 'order [A-za-z \dth]* | may [\d]*'
matches = re.findall(pattern,flipcard_godrej,flags = re.IGNORECASE)
print(matches)


# Extracting n-gram using user-defined-function 
import re
def n_gram_extractor(input_str,n):
    tokens = re.sub(r'([^\s\w] | _)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extractor(flipcard_godrej,4)




