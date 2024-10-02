#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:30:20 2024

@author: Sachin Borade
"""

# EDA
# DATA pre-processing

import pandas as pd
# import dataset 

df = pd.read_csv("csv/ethnic diversity.csv")

## Let's check the data type
df.dtypes

## salaries data type is --float let's convert it into --int
df.Salaries = df.Salaries.astype(int)
df.dtypes
# Now the data type of Salaries is --int 

## similarly the age should be --float
df.age = df.age.astype(float)
df.dtypes
# Now the data type of age is --float

##############################################################################


# importing dataset 

df1 = pd.read_csv("csv/modified ethnic.csv")
df1.dtypes

# Let's find the duplicated 
duplicates = df1.duplicated()
# Output of this function is single column
# If there is duplicate records output -- True
# If there is no duplicate records ouput -- False
# Series will be created
duplicates
sum(duplicates) # no duplicates are there


# importing dataset 
df2 = pd.read_csv("csv/mtcars_dup.csv")
df2.dtypes

# Checking the duplicates
duplicates1 = df2.duplicated()
duplicates1
sum(duplicates1) # 3 duplicates are there 



### There is a function to drop the duplicate values 
df_new = df2.drop_duplicates()

sum(df_new.duplicated()) # Duplicates are removed


#############################################################################

## outlier treatment
import pandas as pd
import seaborn as sns

df = pd.read_csv("csv/ethnic diversity.csv")

# Now let us find the outliers in Salaries 
sns.boxplot(df.Salaries)

# There are outliers 
# Let us check outlier in age column
sns.boxplot(df.age)
# There are no outliers

## Let us Calculate IQR = Q3 - Q1
iqr = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
IQR = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
IQR
# IQR it is capital so it is not going to reflect in variable explorer 
# it is treated as constant.

lower_limit = df.Salaries.quantile(0.25) - 1.5*IQR
upper_limit = df.Salaries.quantile(0.75) + 1.5*IQR

# Now you will see the lower limit of salary is -19446.9675
# Now you will see the upper limit of salary is 93992.8125



#############################################################################

# Trimming 
import numpy as np
outliers_df = np.where(df.Salaries > upper_limit,True,
                       np.where(df.Salaries < lower_limit,True,False))

# you can check outliers_df column in variable explorer
df_trimmed = df.loc[~outliers_df]

df.shape         # (310, 13)
df_trimmed.shape # (306, 13)

import seaborn as sns
sns.boxplot(df_trimmed.Salaries)
# Now you can see all the outliers are removed


#############################################################################

# Replacement Technique
# Drawback of trimming rechnique is we are losing the data 
df = pd.read_csv("csv/ethnic diversity.csv")
df.describe()

# Map all the outliers values to upper limit
df_replaced = pd.DataFrame(np.where(df.Salaries > upper_limit,upper_limit,np.where(df.Salaries < lower_limit,lower_limit,df.Salaries)))

# If the values are greater than upper_limit
# Map it to upper limit and less than lower_limit
# map it to lower_limit if it is within the range
# then keep as it is
sns.boxenplot(df_replaced[0])

#############################################################################

# Winsorization 
import seaborn as sns
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr',tail = 'both',fold=1.5,variables=['Salaries'])
# Copy Winsorizer and paste in Help tab of top right window, study the 
# method
df_t = winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])

#############################################################################

# Zero variance and near zero variance
# If there is no variance in the feature, then ML model will not get any 
# intelligence, so it is better to ignore features
import pandas as pd
df = pd.read_csv("csv/ethnic diversity.csv")
df['Salaries'].var()
# Here EmpID and ZIP is nominal data

df.Salaries.var()==0

# None of them are equal to zero 
df.EmpID.var(axis=0) == 0
df.Zip.var(axis=0) == 0
df.Salaries.var(axis=0) == 0
df.age.var(axis=0) == 0

############################################################################
import pandas as pd
import numpy as np 

df = pd.read_csv("csv/modified ethnic.csv")

# Checking null values 
df.isnull().sum()
'''
Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries            32
age                 35
Race                25
'''

# Create an imputer that creates NaN values 
# mean and median is used for numeric data 
# mode is used for discrete data

from sklearn.impute import SimpleImputer
mean_imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
# Check the dataframe 
df['Salaries'] = pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
# Check the dataframe 
df['Salaries'].isna().sum()
# here we can see all the null values are get replaced by mean 

#### There are outlier in age attribute so we are going to use median 
#   imputer

from sklearn.impute import SimpleImputer
median_imputer = SimpleImputer(missing_values=np.nan,strategy='median')
# Check the dataframe 
df['age'] = pd.DataFrame(median_imputer.fit_transform(df[['age']]))
# Check the dataframe 
df['age'].isna().sum()
# here we can see all the null values are get replaced by mean 

########################################################################

## mode imputer 
mode_imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')

df['Sex'] = pd.DataFrame(mode_imputer.fit_transform(df[['Sex']]))
df['Sex'].isna().sum()

df['MaritalDesc'] = pd.DataFrame(mode_imputer.fit_transform(df[['Sex']]))
df['MaritalDesc'].isna().sum()

########################################################################

import numpy as np

from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
    
# Generate the imbalanced dataset 
X, y = make_classification(n_samples=1000,
                           n_features=20,
                           n_informative=2,
                           n_redundant=10,
                           n_clusters_per_class=1,
                           weights=[0.99],
                           flip_y=0,
                           random_state=1)

'''
        n_samples = 1000
             The total number of samples (data points) to generate 
             Each sample will have 20 features 
             
        n_features =20 
            The total number of features(columns) in the dataset 
            Each sample will have 20 features 
            
        n_informative = 2 
            The number of informative features
            The features are useful for predicting the target variable 
        
    
        n_redundant = 10
            The number of redundunt feature 
            The features ar generated as random linear combinations

'''

# Show original class distribution
print("Original Class Distribution",np.bincount(y))

# Step 2: Apply SMOTE to balance the dataset 
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Show the new class distribution after applying SMOTE 
print("Resampled class distribution: ", np.bincount(y_res))


# Show the original class distribution 
print(f"Original Class distribution : {np.bincount(y)}")


# Step 3: split the data into training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.3,random_state=42)


# Step 4: Apply SMOTE to balance the training dataset 
smote = SMOTE(random_state=42)
X_train_res,y_train_res = smote.fit_resample(X_train, y_train)

# Show the new class distribution after applying SMOTE
print(f"Resampled class distribution :{np.bincount(y_train_res)}")


# Step 5: Train a classifier on the balanced dataset 
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_res,y_train_res)

# Step 6: Evaluate th classifier on the test set 
y_pred = clf.predict(X_test)

print("Confusoin Matrix ")
print(y_test,y_pred)


########################################################################
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt



# Generate a sample dataset 
np.random.seed(0)
data = np.random.exponential(scale=2.0,size=1000)
df = pd.DataFrame(data,columns=['Value'])

# Perform log transformation 
df['LogValue'] = np.log(df['Value'])



# Plot the original and log transformed data 
fig,axes = plt.subplots(1,2,figsize=(12,6))

# Original data 
axes[0].hist(df['Value'],bins=30,color='blue',alpha=0.7)
axes[0].set_title("Original Data")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")


# Log Transformed Data 

axes[1].hist(df['LogValue'],bins=30,color='green',alpha=0.7)
axes[1].set_title("Log_tranformed Data")
axes[1].set_xlabel("Log(Value)")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()















