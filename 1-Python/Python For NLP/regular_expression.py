#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:40:17 2024

@author: Sachin Borade
"""
import re

chat1 = "Hello, I am having an issue with my order #343434 "
## Define the pattern
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern,chat1)
print(matches)

#################

chat2 = "I have problem with my order number 3434343"
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern,chat2)
print(matches)

chat3 = "My order 9875857 is having some issue"
matches = re.findall(pattern,chat3)
print(matches)

#################

## Creating the function for matching the sentence
def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]

get_pattern_match('order[^\d]*(\d*)',chat1)


################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:10:37 2024

@author: Sachin Borade
"""

chat1 = 'you ask lot of questions 1234432144, abc@xyz.com'
chat2 = 'here it is: (123)-567-5678, abc@xyz.com'
chat3 = 'yes, phone: 1234567899 email: abc@xyz.com'
print(get_pattern_match('[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*', chat1))
print(get_pattern_match('[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*', chat2))
print(get_pattern_match('[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*', chat3))

print(get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat1))
print(get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2))
print(get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3))

text = '''
Born	 Elon Reeve Musk
Birth June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)

'''

print(get_pattern_match(r'age (\d+)', text))
print(get_pattern_match(r'Born(.*)\n', text).strip()) #remaining lines are getting stripped out
print(get_pattern_match(r'Born.\n(.)\(age', text))
print(get_pattern_match(r'age.\n(.)', text))

#############################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:12:49 2024

@author: Sachin Borade
"""

elon_musk = '''
Born	 Elon Reeve Musk
Birth June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)

'''

import re
## Creating the function for matching the sentence
def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]


def extract_personal_information(text):
        age = get_pattern_match('age (\d+)', text)
        full_name = get_pattern_match('Born(.*)\n', text)
        birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
        birth_place = get_pattern_match('\(age.*\n(.*)', text)
        return {
                'age':int(age),
                'name':full_name.strip(),
                'birth_date':birth_date.strip(),
                'birth_place':birth_place.strip()
            }
extract_personal_information(elon_musk)

#############################################################################

ambani=""" Born	Dhirubhai Ambani
28 December 1932
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	 6 July 2002 (age 69)
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of Inflipcard_godrej = '''
I ordered godrej 180 l direct cool single door 2 star refrigerator order May 29th 
 received may 30 after 5 days use i write this review this godrej 
refrigerator is enough for 2 or 3 people small family and bachelor cooling 
effect is good freezing ice cubes with in a 3 hours only disappoint i expect 
the class shelf but in this model have grill shelf but disign is okay this
 price over all good 
'''dia (1947–1950)
India (1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)
"""
def extract_personal_information(text):
        age = get_pattern_match('age (\d+)', text)
        full_name = get_pattern_match('Born(.*)\n', text)
        birth_date = get_pattern_match('Born.*\n(.*)', text)
        birth_place = get_pattern_match('\(age.*\n(.*)', text)
        return {
                'age':int(age),
                'name':full_name.strip(),
                'birth_date':birth_date.strip(),
                'birth_place':birth_place.strip()
            }

extract_personal_information(ambani)

#############################################################################

## Reading the pdf files 



# Importing Required Moudles 
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader


# Creating a PDF reader object
reader = PdfReader('kopargaon-part-1.pdf')

#Printing the number of pages in the pdf file 
print(len(reader.pages))

#Getting a specific page from the pdf file
page = reader.pages[1]

#Extracting text from page 
text = page.extract_text()
print(text)


#############################################################################

# Importing Required Moudles 
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

# Creating a PDF reader object
reader = PdfReader('matrix_basics.pdf')

#Printing the number of pages in the pdf file 
print(len(reader.pages))

#Getting a specific page from the pdf file
page = reader.pages[1]

#Extracting text from page 
text = page.extract_text()
print(text)


#############################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:42:43 2024

@author: Sachin Borade
"""
 

import re 
sentence5 = "sharat twitted , wittnessing 68th republic day India from Rajpath, \new Delhi, Mesmorizing performance by India Army!"
re.sub(r'([^\s\w | _ ])+',' ',sentence5).split()

#############################################################################


## EXTRACTING n-grams 
# Can be exracted using 3- Techniques 
# 1. custom defined function 
# 2. NLTK
# 3. TextBlob


#############################################################################

#1. Extracting n-gram using custom defined function 
import re
def n_gram_extractor(input_str,n):
    tokens = re.sub(r'([^\s\w] | _)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extractor("The cute little boy is playing",2)
n_gram_extractor("The cute little boy is playing",3)

#############################################################################

# 1.  Extracting all the websites from twitter handle 

import re

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = 'https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)

#############################################################################

# 2. Extracing the Headline 

text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''

pattern = 'Concentration of Risk: ([^\n]*)'

# Pattern Matching 
re.findall(pattern,text)

#############################################################################

# 3. To extract the quarterly and seasonal period  

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches = re.findall(pattern,text)
matches

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''

pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10} '
matches = re.findall(pattern,text)
matches

#############################################################################

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''


pattern = 'Note \d - ([^\n]*)'
matches = re.findall(pattern,text)
['Overview', 'Summary of Significant Accounting Policies']

#############################################################################

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''

pattern = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern,text)
matches

#############################################################################
    
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''

pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern,text,flags = re.IGNORECASE)
matches

#############################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:31:10 2024

@author: Sachin Borade
"""


# Import n-gram using NLTK

from nltk import ngrams
# Extracting ngrams with nltk 

list(ngrams("The cute littel boy is playing with kitten".split(),2))
list(ngrams("The cute littel boy is playing with kitten".split(),3))

####################################

from textblob import TextBlob
blob = TextBlob("The cute little boy is playing with kitten")
blob.ngrams(n=2)
blob.ngrams(n=3)


#############################################################################

# Tokenization using keras 
sentence5 = "sharat twitted , wittnessing 68th republic day India from Rajpath, \new Delhi, Mesmorizing performance by India Army!"

from tensorflow.keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

#############################################################################

# Tokenization using TextBlob
from textblob import TextBlob
blob = TextBlob(sentence5)
blob.words

#############################################################################

#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer = TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)

#############################################################################

# Multi word tokenizer

'''
multi-word tokenizers are essential for tasks where the meaning of the text
heavily depends on the interpretation of phrases as wholes rather than as 
sums of individual words. 
For instance, in sentiment analysis, recognize "not goot" as single negative 
sentiment unit rather than as "not" and "good" seperately can significantly 
affect th outcome.
'''

from nltk.tokenize import MWETokenizer

sentence5
mwe_tokenizer = MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())



