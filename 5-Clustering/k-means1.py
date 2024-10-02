#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:33:02 2024

@author: Sachin Borade

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Let us try to understand first how k means works for two dimentional data 
# for that, generate random numbers in the range 0 to 1 ad with uniform probability 
# of 1/ 50


X = np.random.uniform(0,1,50)
Y = np.random.uniform(0,1,50)
# Create a empty dataframe with 0 rows and 2 columns
df_xy = pd.DataFrame(columns=["X","Y"])
df_xy.X = X
df_xy.Y = Y  
df_xy.plot(x="X",y="Y",kind="scatter")
model1 = KMeans(n_clusters = 3).fit(df_xy)


'''
with data x and y apply kmeans model,
generate scatter plot 
with scale font=10 

cmap = plt.cm.coolwarn:cool color combination 

'''


model1.labels_
df_xy.plot(x='X',y='Y',c=model1.labels_,kind='scatter',s=10,cmap=plt.cm.coolwarm)


###############################################################################

univ1 = pd.read_excel("csv/University_Clustering.xlsx")
univ1.describe()
univ = univ1.drop(['State'],axis=1)
# We know that there is scale difference among the columns, which we 
# either by using normalization or standardization 

def norm_func(i):
    x = (i-i.min()) / (i.max()-i.min())
    return x
    

# Now apply this normalization function to univ dataframe for all columns 

df_norm = norm_func(univ.iloc[:,1:])
'''
what will be ideal cluster number, will it be 1,2 or 3
'''

TWSS = []
k =list(range(2,8))
for i in k:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(df_norm)

    TWSS.append(kmeans.inertia_) 
    # total within sum of square
    '''
    KMeans inertia, also known as Sum of Squares Erros(or SSE)
    calculates the sum of the distances of all points within a cluster from the 
    centriod of the point. 
    It is difference between the oberserved value and predicted value.
    '''

TWSS

# As k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No of Clusters")
plt.ylabel("Total within SS")



model = KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb = pd.Series(model1.labels_)
univ['clust'] = mb
univ.head()
univ = univ.iloc[:,[7,0,1,2,3,4,5,6]]
univ
univ.iloc[:,2:8].groupby(univ.clust).mean()

univ.to_csv("csv/kmeans_university.csv",encoding='utf-8')
import os 
os.getcwd()






















