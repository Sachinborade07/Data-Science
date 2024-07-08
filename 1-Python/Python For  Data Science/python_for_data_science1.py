#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:11:36 2024

@author: Sachin Borade
"""


'''
A series id used to model one dimensional data,
similar to a list in python.
The series object also ha a few more bits
of data, including an #index and a name.
'''

import pandas as pd
songs = pd.Series([145,142,38,13],name = "counts")
songs.index
#The index can be string based as well

songs2 = pd.Series([145,142,38,13],name = "counts", index = ["paul","john","jeorge","ringo"])
songs2.index
songs2


# Reading the csv files

import pandas as pd
f1 = pd.read_csv("/home/sachin/Desktop/Data Science/1-Python/csv_files/age.csv")
f1

df = pd.read_excel("/home/sachin/Desktop/Data Science/1-Python/csv_files/Bahaman.xlsx")
# None, NaN, nan, and null are synonyms 
# The series object behaves similarly to a  Numpy array

import numpy as np
numpy_ser = np.array([145,142,38,13])

songs2[1] #142
numpy_ser[1] #142

#They both have Methods in common
songs2.mean()
numpy_ser.mean()
# Both have same output ## 84.5



## The pandas series data structure provides support for "CURD" operatin 

## CREATE ## READ ## UPDATE ## DELETE 


## CREATION OF DATAFRAME
arijit = pd.Series([10,7,1,22], index = ['2007','2009','2012','2012'],
                       name = 'Arijit_Songs')
arijit

############################################################################


## READING ON DATAFRAME 
 
arijit['2007'] #10
arijit['2012'] #2012     1
               #2012    22

# We can iterate over data in a series as well. When iterating over a series
for item in arijit:
    print(item)

############################################################################


##  UPDATING ON DATAFRAME
# updating values in a series can be a little tricky as well
arijit['2007'] = 40
arijit['2007']


############################################################################

## DELETING ON DATAFRAME
# The del statement appears to have problem with duplicate index
import pandas as pd
s = pd.Series([2,3,4],index = [1,2,3],name="Position")
print(s)
''' 
1    2
2    3
3    4
'''
del s[1]
'''
2    3
3    4
'''
print(s)


############################################################################

## Converting Data Types

# Sting use.astype(str)
# numeric use pd.to_numeric
# integer use.astype(int)
# Note:- that this will fail with NaN
# datetime use pd.to_datetime


songs_66 = pd.Series([3.0,None,11.0,9.0],
                     index = ["sachin","om","sai","ram"],
                     name = "Counts")
songs_66.dtypes

## Changing float to string datatype
pd.to_numeric(songs_66.apply(str))
## There is error 
## we cannot convert none type into the string so,
pd.to_numeric(songs_66.apply(str),errors='coerce')
# If we pass errors = 'coerce'
# We can see that it supports many fromats
songs_66.dtypes


### Dealing with None value
# The .fillna mehtod will replace them with a given value
songs_66 = songs_66.fillna(-1)
songs_66.dtypes


## Changing the datatype float to string
# This time it will not give us the error
songs_66 = songs_66.astype(str)
songs_66.dtypes


## We can also drop the NULL values form series using 
## .dropna() method 

songs_66 = pd.Series([3.0,None,11.0,9.0],
                     index = ["sachin","om","sai","ram"],
                     name = "Counts")
songs_66 = songs_66.dropna()
songs_66
## We can see all the null values are get dropped 


############################################################################


## Appending , Combining and Joining two series 

#Series1
songs_66 = pd.Series([3.0,None,11.0,9.0],
                     index = ["sachin","om","sai","ram"],
                     name = "Counts")

#Series2
songs_69 = pd.Series([7,None,8,22],
                     index = ["ram","sham","ghansham","krishna"],
                     name = "Counts")


# To caoncatenate two series together, simply by using .append() method
songs = pd.concat([songs_66,songs_69])
songs


############################################################################


## Plotting the series using matplotlib.pyplot

import matplotlib.pyplot as plt 

songs_69 = pd.Series([7,16,21,51],
                     index = ["ram","sham","ghansham","krishna"],
                     name = "Counts")

fig = plt.figure() # Initilizing the figure
songs_69.plot()
plt.legend()

#####################
# plotting the bar graph for the same 
fig = plt.figure()
songs_69.plot(kind='bar')
#Changing the color of bar graph 
songs_66.plot(kind='bar',color='r')
plt.legend()

############################################################################

import numpy as np
data = pd.Series(np.random.randn(500),name = "500_random")
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
''' 
ax = fig.add_subplot(111) is a way to add a (1 x 1) grid of subplots to a figure in Matplotlib, 
and returns the first axis object in the grid.
 The default argument is 
 fig.add_subplot(1, 1, 1), which adds one axes in a one row by one column axes grid.
 You can also use an alternative format 
 with a three-digit integer without a comma, such as fig.add_subplot(111)
 
'''

# What is Pandas DataFrame?
# Pandas Dataframe is a Two-Dimentional data structure,
# an immutable, heterogeneous tabular data structure with labeled 
# axed rows and column

import pandas as pd
pd.__version__


#Create using constructor 
# Create pandas dataframe from list 
import pandas as pd
technology = [ ["spark",20000,"30days"],
              ["pandas",30000,"40days"]
             ]
df = pd.DataFrame(technology)
df

# Since we have not given labels to columns and indexes,
# Dataframe by default asssign increamental sequence numbers as labels
#to both rows and columns, these are called Index.


# Adding Column & Row lables to DataFrame

column_name = ["courses","fee","Duration"]
row_label = ["a","b"]
df = pd.DataFrame(technology,columns=column_name,index=row_label)
df


## Checking the data type of DataFrame
df.dtypes

# You can also assign custom datatype to columns 
# Set custom type to DataFrame

import pandas as pd
technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
        'Fee':[2000,2032,2320,4349,5454,4545,4545],
        'Duration':["30days","40days","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]            
}

df = pd.DataFrame(technology)
print(df.dtypes)

# Converting all types to best possible types
df2 = df.convert_dtypes()
df2.dtypes
# Change all columns to same type
df = df.astype(str)
print(df.dtypes)
# Change Type for one or multiple columns
df = df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#Convert Data Type for All Columns in a List 
df = pd.DataFrame(technology)
df.dtypes
cols = ["Fee","Discount"]
df[cols] = df[cols].astype('float')
df.dtypes

#Ignore Errors 
df = df.astype({"Courses":int },errors="ignore")
df.dtypes
# Generates Errors
df = df.astype({"Courses":int },errors="raise")

# Converts feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount'])
df.dtypes


## Convert DataFrame to csv file

df.to_csv('data_file.csv')
# Now we can see in the csv file in our working directory 

# Create Dataframe from csv file 
df = pd.read_csv('data_file.csv')

#############################################################################

# Pandas DataFrame - Basic Operations 
# Create DataFrame with None/NULL to work  with examples
import pandas as pd 
import numpy as np

technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days"," ","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

row_label = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technology, index=row_label)
print(df)

#############################################################################

# Data Frame Porperties
df.shape
#  (8, 4)

df.size
#32

df.columns
# Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')

df.columns.values
# array(['Courses', 'Fee', 'Duration', 'Discount'], dtype=object)

df.index
# Index(['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'], dtype='object')

df.dtypes

df.info

##############################################################################

## Accessing one column contents
df['Fee']

## Accessing two column contents
cols = ['Fee','Duration']
df[cols]
## OR
df[['Fee','Duration']]

## Select certain rows and assign to another DataFrame

df2 = df[6:]
print(df2) ## It will start from 6 to last
'''  Courses     Fee     Duration    Discount
r6    None      4545.0   70days      18.4
r7    Java      4545.0   90days      19.5
'''


df2 = df[:6]
df2   ## It will start from 0 and goes till 6

'''     Courses     Fee Duration  Discount
r0    Spark  2000.0   30days      11.8
r1  PySpark  2032.0   40days      23.7
r2   Hadoop  2320.0               13.4
r3   Python  4349.0   35days      15.7
r4   Pandas     NaN   25days      12.5
r5   Oracle  5454.0   60days      25.4
'''

## Accessing certain cell from DataFrame ('Duration') 
df['Duration'][3]

## Subtract Specific value from column
df['Fee'] = df['Fee'] - 500
df['Fee']

## Pandas to manipulate DataFrame
## Describe DataFrame for all numeric columns
df.describe()
'''              Fee   Discount
count     7.000000   8.000000
mean   2606.428571  17.550000
std    1439.971164   5.115523
min    1000.000000  11.800000
25%    1176.000000  13.175000
50%    3349.000000  17.050000
75%    3545.000000  20.550000
max    4454.000000  25.400000
'''
## It will give us the 5 number summary 

##############################################################################

# rename() - Renames pandas DataFrame columns

df = pd.DataFrame(technology,index=row_label)

# Assign new header by setting new columns names.
df.columns=['A','B','C','D']
df

## Rename Column Names using rename() method

df = pd.DataFrame(technology,index=row_label)
df.columns=['A','B','C','D']

df2 = df.rename({'A':'c1','B':'c2'},axis=1)
df2
#one more method
df2 = df.rename({'C':'c3','D':'c4'},axis='columns')
df2
#one more method
df2 = df.rename(columns={'A':'c1','B':'c2'})
df2

##############################################################################

# initilized the DataFrame everytime
df = pd.DataFrame(technology,index=row_label)

## Drop DataFrame Rows and Columns

## ROWS

# Drop rows by labels
df1 = df.drop(['r1','r2'])
df1

# Delete rows by position/ index
df = pd.DataFrame(technology,index=row_label)
df1 = df.drop(df.index[1])
df1

df1 = df.drop(df.index[[1,3]])
df1

# Delete rows by Index Range
df1 = df.drop(df.index[2:])
df1

# When you have default indexes for rows
df = pd.DataFrame(technology)
df1 = df.drop(0)
df1

df = pd.DataFrame(technology)
df1 = df.drop([0,3],axis=0) # It will delete row0 and row3
df1

df1 = df.drop(range(0,2)) # It will delete 0 and 1
df1

## COLUMNS

import pandas as pd 
import numpy as np

technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days"," ","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}


df = pd.DataFrame(technology)
## Dropping column
df2 = df.drop(['Fee'],axis=1)
df2 # Here the changes will occur in another dataframe


# Alternatively you can also use columns instead of labels
df2 = df.drop(columns=['Fee'],axis=1)

#Drop column by index
print(df.drop(df.columns[2],axis=1))
df

# You can see the changes are occured temporarily
# to do it permanenet
# inplace = True / False :- is the parameter which will permenently
#           or temporarily do the changes in the DataFrame
df.drop(df.columns[2],axis=1,inplace=True)
df


# Drop two or more column by label name
df2 = df.drop(['Courses','Fee'],axis=1)
print(df2)
    
#############################################################################


#Dropping two or more column by index
df = pd.DataFrame(technology)
df2 = df.drop(df.columns[[0,1]],axis=1)

#Dropping columns from list of columns
df = pd.DataFrame(technology)
df.columns
list_col = ['Courses','Fee']
df2 = df.drop(list_col,axis=1)
df2

##############################################################################


import pandas as pd
import numpy as np
technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days","70days","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

row_label = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technology, index=row_label)
print(df)


# Below are quick example 
df2 = df.iloc[:,:2]
df2

# This line used the slicing operator to get DataFrame item by index
# The first slice [:] indicated to return all rows.
# The second slice specifies that only columns between 0 and 2 should be returned

df2 = df.iloc[0:2,:]
df2

# In this case, it will first slice [0:2]
# The second slice [:] will take all the columns

# Slicing specific Rows and Columns using iloc attribute
df3 = df.iloc[1:2,1:3]
df3

### Select rows by integer index 
df2 = df.iloc[2]
df2


## Want only specific set of rows

df2 = df.iloc[[2,3,6]] # Select rows by index as 2,3,6
df2
df2 = df.iloc[1:5]  # Select rows by integer index range
df2
df2 = df.iloc[:1] # Select the first row only
df2
df2 = df.iloc[:3] # Select first 3 rows only 
df2
df2 = df.iloc[-1:] # Select last row
df2
df2 = df.iloc[-3:] # Select last 3 rows
df2
df2 = df.iloc[::2] # Select alternate rows with step of 2
df2



### Select rows by (loc) by Index Labels
df2 = df.loc[['r2']] # Selecting rows by index lables
print(df2)
df2 = df.loc[['r1','r2','r3']] # Selecting rows by list containing name of rows 
df2

df2 = df.loc['r1':'r5']
df2  # Select rows labels with index range from r1 to r5

##############################################################################

import pandas as pd
import numpy as np
technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days","70days","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

row_label = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technology, index=row_label)
print(df)


### Select column by (loc) by Index Labels
# loc[] syntac to slice columns
# df.loc[:,start:stop:step]
# In loc we give parameter as Index Labels.


# Selecting multiple columns
df2 = df.loc[:,['Courses','Fee','Discount']]

# Selecting random columns
df2 = df.loc[:,['Courses','Discount','Fee']]
df2

# Selecting column between two column
df2 = df.loc[:,'Fee':'Discount']
df2

# Selecting column by range
df2 = df.loc[:,'Duration':]
df2 # It will select column from ('Duration') onwards 

# Selecting column by range
df2 = df.loc[:,:'Duration']
df2 # It will select column upto ('Duration') 

# Selecting column by the step of 2
df2 = df.loc[:,::2]
df2


##############################################################################
# Pandas.DataFrame.query() by Examples
# Query all which is equals with Courses == 'PySpark'

df2 = df.query("Courses == 'PySpark' ")
df2

# Query all rows which is not equals  like Courses != 'PySpark'

df2 = df.query("Courses != 'PySpark' ")
df2

##############################################################################


import pandas as pd
import numpy as np
technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days","70days","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

row_label = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technology, index=row_label)
print(df)

# Pandas add column to DataFrame
tutors = ['ram','sham','om','rohit','bhagyashree','rohini','sachin','rhutuja']
df2 = df.assign(TutorsAssigned = tutors)
df2

# Add multiple column to the DataFrame 
mnc_companies = ['Tata','birla','amazon','HCL','Google','JIO','Relience','MS']
df2 = df.assign(MNC = mnc_companies,tutor = tutors)
df2

## Derive new column from existing columns 
df = pd.DataFrame(technology)
df2 = df.assign(Discount_percentage = lambda x: x.Fee * x.Discount / 100)
df2
# x.Fee and x.Discount --> while iterating accessing single value of Fee and Discount 

# Append  column to existing pandas DataFrame
# Add new column to the existing DataFrame

df = pd.DataFrame(technology)
df["MNC_Companies"] = mnc_companies
df

### Adding column at specific location
df.insert(0,'Tutors',tutors)
df

###############################################################################


import pandas as pd
import numpy as np
technology = {
        'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days","70days","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

row_label = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technology, index=row_label)
print(df)

## Renaming the single columns
df2 = df.rename(columns={'Courses':'Courses_List'})
df2
## Renaming the multiple columns 

df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee','Duration':'Course_Duration'},inplace=True)
df.columns

"""
Created on Mon Apr 15 08:41:01 2024

@author: sachin borade
"""

# Quick example of getting the number of rows and columns

rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count
column_count = len(df.axes[1])
column_count

df = pd.DataFrame(technology)
row_count = df.shape[0]
row_count
col_count = df.shape[1]
col_count



#using DataFrame.apply() to appply function add column

import pandas as pd
import numpy as np

data ={
         "A":[1,2,3],
         "B":[4,5,6],
         "C":[7,8,9]
       }

df = pd.DataFrame(data)
df


def add_3(x):
    return x+3
df2 = df.apply(add_3)
df2

## Applying of individual column
df2 = ((df.A).apply(add_3))
df2  ## here only one column get displayed

######################################

def add_4(x):
    return x+4
df["B"] = df["B"].apply(add_4)
df["B"] ## here all column are getting displayed

## apply multiple column

df[["A","B"]] = df[["A","B"]].apply(add_4)
df

# apply a lambda function to each column

df2 = df.apply(lambda x: x + 10)
df2  #now we can see the operation is applicable to each column


######################################
# apply() function on selected list of multiple columns
df = pd.DataFrame(data)
df[["A","B"]] = df[["A","B"]].apply(add_3)
df
######################################
# apply() lambda function to single column
# Using Dataframe.apply() and lambda function


df2["A"] = df["A"].apply(lambda x: x + 10)
df2

######################################
# Using pandas.DataFrame.transform() to apply function 
# using DataFrame.transform()

df = pd.DataFrame(data)

def add_2(x):
    return x + 2
df = df.transform(add_2)
df
#######################################
# Using pandas.DataFrame.map() to single column

df = pd.DataFrame(data)
df['A'] = df['A'].map(lambda A:A/2)
df
#######################################
# Using numpy function on single column
# using DataFrame.apply() & [] operator
import numpy as np
df = pd.DataFrame(data)
df['A'] = df['A'].apply(np.square)
df

# Another method
df['A'] = np.square(df['A'])
df
#######################################

# pandas groupby() with examples 
import pandas as pd
import numpy as np
technology = {
        'Courses':["Spark","Python","Hadoop","Python","Pandas","Pandas",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days"," ","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

df = pd.DataFrame(technology)
df

# Use groupby() to compute the sum
df2 = df.groupby(['Courses']).sum()
df2
# We can see we have multiple duplicate entries but with the help of groupby() 
# we are able to get only single entry at a time. 

# Groupby multiple columns
df2 = df.groupby(['Courses','Fee']).sum()
df2

# Add index to grouped data 
# Add row index to the group by result
# if we see the before result the index are in jumbled form and our indexes 
# were ['Courses','Fee']
# to make index in setted form we use reset_index() function.
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
df2


###################################

## Get the list of all columns names from headers
column_headers = list(df.columns.values)
print("The Column Headers:",column_headers)
## Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers


###########################################################################

#Pandas Shuffle Dataframe Rows
import pandas as pd
technology = {
        'Courses':["Spark","Python","Hadoop","Python","Pandas","Pandas",None,"Java"],
        'Fee':[2000,2032,2320,4349,np.nan,5454,4545,4545],
        'Duration':["30days","40days"," ","35days","25days","60days","70days","90days"],
        'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4,19.5]            
}

df = pd.DataFrame(technology)
print(df)


## pandas shuffle dataframe rows
# shuffle the dataframe rows and return all columns
df1 = df.sample(frac=1)
df1 = df.sample(frac=0.5)
df1 = df.sample(frac=0.7)
print(df1)

## Create a new Index starting from zero after shuffling
df1 = df.sample(frac=1).reset_index()
df1
df1 = df.sample(frac=1).reset_index(drop=True)
df1



###########################################################################
# Joining two dataframe 
import pandas as pd
technology1 = {
        'Courses':["Spark","PySpark","Python","Pandas"],
        'Fee':[2000,2032,2320,4349],
        'Duration':["30days","40days","35days","25days"]
}
index_labels1 = ['r1','r2','r3','r4']
df1 = pd.DataFrame(technology1,index=index_labels1)
technology2 ={
        'Courses':["Spark","Java","Python","Go"],
        'Discount':[11.8,23.7,13.4,15.7]  
}
index_labels2 = ['r1','r6','r3','r5']
df2 = pd.DataFrame(technology2,index_labels2)


# pandas join
df3 = df1.join(df2,lsuffix='_Left',rsuffix='_right')
df3
# By default it is left join
'''
 Courses_Left   Fee Duration Courses_right  Discount
r1        Spark  2000   30days         Spark      11.8
r2      PySpark  2032   40days           NaN       NaN
r3       Python  2320   35days        Python      13.4
r4       Pandas  4349   25days           NaN       NaN

'''
###########################################################################

# pandas inner join on dataframe
df3 = df1.join(df2,lsuffix='_Left',rsuffix='_right',how='inner')
df3
# It will not take the null values
'''
 Courses_Left   Fee Duration Courses_right  Discount
r1        Spark  2000   30days         Spark      11.8
r3       Python  2320   35days        Python      13.4
'''
###########################################################################

# pandas left join on dataframe
df3 = df1.join(df2,lsuffix='_Left',rsuffix='_right',how='left')
df3
# left join
# left values not be null
'''
Courses_Left   Fee Duration Courses_right  Discount
r1        Spark  2000   30days         Spark      11.8
r2      PySpark  2032   40days           NaN       NaN
r3       Python  2320   35days        Python      13.4
r4       Pandas  4349   25days           NaN       NaN
'''
###########################################################################

# pandas right join on dataframe
df3 = df1.join(df2,lsuffix='_Left',rsuffix='_right',how='right')
df3
# right values not be null
'''
Courses_Left     Fee Duration Courses_right  Discount
r1        Spark  2000.0   30days         Spark      11.8
r6          NaN     NaN      NaN          Java      23.7
r3       Python  2320.0   35days        Python      13.4
r5          NaN     NaN      NaN            Go      15.7
'''

###########################################################################

# joining using pandas merge method
df3 = pd.merge(df1,df2)
df3
## Same as inner join but columns are not repeating 

'''
Courses   Fee Duration  Discount
0   Spark  2000   30days      11.8
1  Python  2320   35days      13.4
'''

## or
df3 = df1.merge(df2)
df3

###########################################################################

import pandas as pd

df = pd.DataFrame({
        'Courses':["Spark","PySpark","Python","Pandas"],
        'Fee':[20000,25000,22000,24000]
    })
df1 = pd.DataFrame({
        'Courses':["Pandas","Hadoop","Hyperion","Java"],
        'Fee':[25000,25200,24500,24900],
    })

# using concat() method
data = [df,df1]
df2 = pd.concat(data)
df2

#########################################################################

#Concatenating multiple dataframe


df = pd.DataFrame({
        'Courses':["Spark","PySpark","Python","Pandas"],
        'Fee':[20000,25000,22000,24000]
    })
df1 = pd.DataFrame({
        'Courses':["Pandas","Hadoop","Hyperion","Java"],
        'Fee':[25000,25200,24500,24900],
    })
df2 = pd.DataFrame({
        'Duration':["30days","40days","35days","25days","55days"],
        'Discount':[11.8,23.7,13.4,15.7,75] 
    })

# appending multiple dataframe
df3 = pd.concat([df1,df2,df3])
df3


## Reading the excel file
import pandas as pd
df = pd.read_csv("/home/sachin/Desktop/Data Science/1-Python/Python For Data Science/data_file.csv")


# Using Series.values.tolist()
col_list = df.Courses.values
print(type(col_list)) # The type of list is <class 'numpy.ndarray'>
print(col_list)
col_list = df.Courses.values.tolist()
print(type(col_list)) # The type of list is <class 'list'>
print(col_list)

# Using list function
col_list = list([df["Courses"]])
print(type(col_list))

# convert to numpy array
col_list = df['Courses'].to_numpy()
col_list




