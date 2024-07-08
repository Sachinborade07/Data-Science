#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:43:01 2024

@author: Sachin Borade
"""

sentence = "we are learning TextMining from Sanjivani AI"


# To find the index of the word
sentence.index("learning")
# It will show the position of learning 


#  We want to know the position of learning 
sentence.split().index("learning")


# Suppose we want to print any word in reverse order 
sentence.split()[2][::-1]
# 'gninrael'

# Suppose we want to print first and last word of the sentece
words = sentence.split() # Tokenization 
words  # ['we', 'are', 'learning', 'TextMining', 'from', 'Sanjivani', 'AI']

first_word = words[0]
first_word
last_word = words[-1]
last_word

# Concatenate the fist and last word 
concat_word = first_word+" "+last_word

# We want to print even words from the sentence 
[words[i] for i in range(len(words)) if i%2==0 ]

# now we want to print print only AI 
sentence[-2:]


# Suppose we want to display sentence character in reverse order 
sentence[::-1]
# 'IA inavijnaS morf gniniMtxeT gninrael era ew' 

# Suppose we want to select each word and print in reversed order 
words = sentence.split()
[words[i][::-1] for i in range(len(words)) ]
# OR 
print(" ".join(word[::-1]for word in words))

#############################################################################

# Tokenization 
import nltk
nltk.__version__
nltk.download('punkt')

from nltk import word_tokenize
words = word_tokenize("I am reading NLP Fundamentals")
print(words)

#############################################################################
# Parts of Speech 
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)

#############################################################################

# Stop words from NLTK library 
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# You can verify there are 179 stopwords in English
print(stop_words)

#############################################################################

# Suppose we want to replace words in string 
sentence1 = "I visited MY from IND on 13-6-24"
normalized_sentence = sentence1.replace("MY","Malayasia").replace("IND","India")
normalized_sentence = normalized_sentence.replace("-24","-2024")
print(normalized_sentence)

#############################################################################

# Suppose we want to autocorrect the sentence 
from autocorrect import Speller 
# define the function spell defined for English 
spell = Speller(lang='en')
spell("Engillish")

#############################################################################

import nltk 
nltk.download('punkt')
from nltk import word_tokenize 
sentence3 = "Ntural Lnguage procesing deall within th arrt of englishh"
# first tokenize the sentence
spell = Speller(lang='en')
sentence3 = word_tokenize(sentence3)
corrected_sentence = " ".join([spell(word) for word in sentence3])
print(corrected_sentence)

#############################################################################

# Stemming 
import nltk
stemmer = nltk.stem.PorterStemmer()
stemmer.stem("programing")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")

#############################################################################

# Lematizing 
# LEMATIZER LOOKS INTO DICTONARY WORDS 
 
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("programing")
lemmatizer.lemmatize("batting")

#############################################################################

# Chunking (Shallow Parsing) Identifying named entities
nltk.download('maxent_ne_chunker')
nltk.download('words')
sentence = "We are Learning NLP in python by SanjivaniAI"
## First we will tokenize
nltk.download('averaged_perceptron_tagger')
words = word_tokenize(sentence)
words = nltk.pos_tag(words)
i = nltk.ne_chunk(words,binary=True)
[a for a in i if len(a) == 1]



#############################################################################
# Sentence tokenization 
from nltk.tokenize import sent_tokenize
sent = sent_tokenize("We are learning NLP in python. Deep Learning in also python.")
sent

#############################################################################

# He went to bank and checked account it was almost 0
# looking this he went to river bank and was crying 
from nltk.wsd import lesk
sentence1 = "keep your saving in the bank "
print(lesk(word_tokenize(sentence1),'bank'))

sentence2 = "It is risky to drive over the river banks or river"
print(lesk(word_tokenize(sentence2),'bank'))








