#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 09:40:27 2024

@author: Sachin Borade
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_excel("csv/University_Clustering.xlsx")
# If you are getting error while reading the file 
'''
ImportError: Pandas requires version '3.1.0' or newer of 'openpyxl'
 (version '3.0.10' currently installed).
 pip uninstall openpyxl
 pip install openpyxl
'''
## From here Business Understanding, what to Minimize and Maximize is remaining
## 


df = df1.drop(['State'],axis=1)
# As state column is not very useful with our dataset 
# We know there are scale difference among the columns which we have to remove
# Either by using Normalization or Standardization.


# Whenever there is mixed data apply normalization

def norm_func(i):
    x = (i - i.min()) / (i.max() - i.min())
    return x

# Now apply this normalization function to dataframe for all the rows and columns 
# from 1 column to end 
#since 0 the column has university name hence skipped
df_norm=norm_func(df.iloc[:,1:])

# You can check df_norm dataframe which is scaled between 0 to 1 
# You can apply describe() function to new dataframe
b = df_norm.describe()

# Before you apply clustering  you need to plot dendogram first 
# Now to create dendogram we need to measure distance
# We have to import linkage 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

# linkage function gives us hierarchical or aglomerative clustering 
# ref the help for linkage 
z = linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering Dendrogram ");
plt.xlabel("Index")
plt.ylabel("Distance")
# ref help of dendrogram 
# sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

# Dendrogram()
# applying agglomerative clustering choosing 5 as cluster from dendrogram 
# whatever has been displayed in dendrogram is not clustering 
# It is just showing number of possible cluster 
from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,linkage='complete',
                                     metric='euclidean').fit(df_norm)

# apply lables to the cluster
h_complete.labels_
cluster_labels = pd.Series(h_complete.labels_)
# Assign this series to df Dataframe as column and name 
df['clust'] = cluster_labels

# We want to relocate the column 7 to 0th position 
df1 = df.iloc[:,[7,1,2,3,4,5,6]]
# now check the df1 dataframe
df1.iloc[:,2:].groupby(df.clust).mean()
# from the output cluster 2 has got highest top10 
# lowest accept ratio, best faculty ratio and highest expenses 
# highest gradutes ratio
df1.to_csv("University.csv",encoding='utf-8')
# from the output cluster 2 has got highest TOP10


'''
Interpretation of the Table:
Rows (Clusters 0, 1, 2):

The rows represent the different clusters (0, 1, 2) identified by the clustering 
algorithm. Each row shows the average values of the columns for that particular cluster.
Columns (Top10, Accept, SFRatio, Expenses, GradRate):

These columns represent different features or attributes in the dataset,
 and the values are the means of these attributes for the corresponding cluster.
Example Interpretation:
    
 -- Cluster 0:

-The average Top10 percentage (percentage of students from the top 10% of their 
                              high school class) is approximately 78.82.
-The average acceptance rate (Accept) is 39.18%.
-The average student-faculty ratio (SFRatio) is 12.82.
-The average expenses (Expenses) for students are approximately $21,446.91.
-The average graduation rate (GradRate) is 87.64%.

-- Cluster 1:

-Top10: 38.75%
-Accept: 70.00%
-SFRatio: 19.25
-Expenses: $9,953.00
-GradRate: 71.75%

-- Cluster 2:

-Top10: 89.00%
-Accept: 26.90%
-SFRatio: 10.00
-Expenses: $40,897.20
-GradRate: 91.70%
-Each cluster represents a group of data points (e.g., universities, schools) 
  that share similar characteristics, as determined by the clustering algorithm. 
-The table summarizes the average characteristics of each cluster.


'''









