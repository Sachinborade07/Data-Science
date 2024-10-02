#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:32:40 2024

@author: Sachin Borade
"""

from bs4 import BeautifulSoup as bs
import requests 
link = 'https://m.imdb.com/title/tt0068646/reviews?ref_=tt_urv'
page = requests.get(link)
page 
page.content
soup = bs(page.content,'html.parser')
print(soup.prettify())  
############################################################

title = soup.find_all('a',class_='title')
title
review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:] = [title.strip('\n') for title in review_title]
review_title
len(review_title)

 
# Let's find out the rating of the movie 

rating = soup.find_all('span',class_='point-scale')
rating
rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:] = [r.strip('/') for r in rate]
len(rate)
rate.pop()
# pop till we will get the same length as we want 
len(rate)

#####################################################

# Now Let's scrap the review body 

review = soup.find_all('div',class_='text')
review
review_body = []
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
# Here we got 25 review body 
# now we have to save the data into the csv file 


import pandas as pd
df = pd.DataFrame()
df['Review_Title'] = review_title
df['Rate'] = rate
df['Review'] = review_body
df

## to_csv
df.to_csv('csv/GodFather.csv')
######

#############################################################


# Sentiment Analysis
import pandas as pd 
from textblob import TextBlob
sent = "This is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol
df = pd.read_csv('csv/GodFather.csv')
df.head()
df['polarity'] = df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
