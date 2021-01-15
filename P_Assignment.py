# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:49:58 2020

@author: RASHMI
"""




#  1. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#  Sample data : 3, 5, 7, 23

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


#   2. Write a Python program to display the first and last colors from the following list.
#   color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
type(color_list)
print(color_list[0])
print(color_list[3])

#  3. Write a Python program to print the even numbers from a given list.
#  sample_list : [1, 2, 3, 4, 5, 6, 7, 8, 9]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in sample_list:
    if i%2==0:
        print("Even number is:", i)
        
        
        
#*****************************************************************************        
#Module  

# 1. Write a Python program to calculate number of days between two dates.      
  #Hint: use Datetime package/module.
  
from datetime import date
f_date=date(2014,7,2)
l_date=date(2014,7,14)
no_of_days=l_date-f_date
print(no_of_days)


#*****************************************************************************
#  III.Functions:
    
#  1. Write a Python program to get the volume of a sphere with radius 6.

pi=3.141
r=6
v=4/3*pi*r**3
print("The volume of sphere is:",v)


#  2. Write a Python program to calculate the sum of three given numbers, 
   #if the values are equal then return three times of their sum 
   #hint: write User defined functions


x=input("enter first value:",)
y=input("enter second value:",)
z=input("enter third value:",)

def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


#   3.Write a Python program to count the number 4 in a given list.
List = [1,4,6,8,4,9,4]
   
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


# 4. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editorSample numbers list :
  #399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
  #815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
  #958,743, 527]

values = (399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
958,743, 527)

for value in values:
    if value==237:
        print(value)
        break;
    elif value%2==0:
        print("even number is:", value)
        
        
        
        
#  5. Write a Python program to find those numbers 
   #which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)        
        
   
value=range(1500,2700)
for i in value:
    if (i%7==0) and (i%5==0):
        print(i)
    
   
#6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5
     
           
for i in range(6):
    if (i==3 or i==6):
        continue
    print(i, end=" ")

    
        
        
# 7. Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
        #for(i=2;i<number;++i)
        
x=0
y=1
while y<50:
   print(y)
   x,y=y,x+y
   
   
#8. Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

    
x=0
y=1
while y<50:
   print("The fibonacci numbers are:", y)
   x,y=y,x+y
    
        

# 9. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

    
#*****************************************************************************    
#IV.STRINGS:
#   1. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))
print(concatenate_list_data(["Kamal"," ","Hassan","  ","Ranjana","Rahul"]))

#***********************************************************************
#  V.Dictionariy:
    
# 1. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


d1={1:2,3:4}
d2={5:6,7:9}
d3={10:8,13:22}
d4 = {**d1, **d2, **d3}
print(d4)

#*******************************************************************
#  VI.Series:
    
# 1. Write a Python program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]


import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 // ds2
print(ds)

#*********************************************************
#  VII.Data Frame:
    
# 1.  Write a Pandas program to select the specified columns and rows from a given data frame. Go to the editorSample Python dictionary data and list labels:
#Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
             
df=pd.DataFrame(exam_data)
labels =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df['labels']=labels
print(df)
df=pd.DataFrame(exam_data, index=labels)
print(df)
print(exam_data['name'])

print(exam_data['name'][1])
print(df.iloc[[1,3,5,6],[0,1]])


#******************************

#  2. Use Crime dataset from LMS
#  I) find the aggregations like all moments of business decisions for all columns,value counts.
#  II) do the plottings like plottings like histogram, boxplot, scatterplot, barplot, piechart,dot chart.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

df1=pd.read_csv("D:\ExcelR\Python\Assignment\crime_data.csv")
df1




df1.rename( columns={'Unnamed: 0':'Country_Name'}, inplace=True )
df1


# I Agrigation
df1.describe()
df1.dtypes
df1.isnull().sum()
df1.describe(include=['O'])
df1['Rape'].value_counts()
df1['Assault'].value_counts()


# II. Plot

#bar plot
sns.barplot(x=df1['Rape'], y=df1['Country_Name'])
plt.title("Crime_Data")
plt.xlabel('Rape rate')
plt.ylabel('Country')
plt.show()


#scatter plot
sns.scatterplot(x=df1['Assault'].values,y=df1['Country_Name'])
plt.title('Crime Info')
plt.ylabel('Assault rate')

# boxplot
sns.boxplot(x=df1["Country_Name"], y=df1['Murder'].values)
plt.title('Crime info')
plt.ylable('Murder rate')

sns.boxplot(x=df1['Murder'].values, y=df1["Country_Name"])
plt.title('Crime info')
plt.ylable('Murder rate')


# boxplot, scatterplot, barplot, piechart,dot chart



import plotly.express as px

df1=pd.read_csv("D:\ExcelR\Python\Assignment\crime_data.csv")
df1
df1.rename( columns={'Unnamed: 0':'Country_Name'}, inplace=True )
df1

country_data = df1["Country_Name"]
crime_data = df1["Rape"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0)  
plt.pie(crime_data, labels=country_data, explode=explode, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Crime")
plt.show()


#*****************************************************************************


#  3. use mtcars dataset from LMS
# A) delete/ drop rows-10 to 15 of all columns
# B)drop the VOL column
# C)write the forloop to get value_counts of all cloumns


import pandas as pd

mtcars=pd.read_csv('E:\Python\Assignment\mtcars.csv')
mtcars

#A  Drope rows-10 to 15 of all columns
mtcars.drop([10,11,12,13,14,15],axis=0,inplace=False)
mtcars

#B   Drop the VOL column
mtcars.drop(['cyl'], axis=1)   #There is no vol column in mtcars


mtcars.head()
mtcars.drop(["disp"], axis = 1)


#C. Value_counts
for col in mtcars.columns:
    print('-' *  0 + col + '-' * 0,  end=' - ')
    display(mtcars[col].value_counts())

#*************************************************************
#4. Use Bank Dataset from LMS
#A)change all the categorical columns into numerical by creating Dummies and using label encoder.
#B) rename all the column names DF
#C) Rename only one specific column in DF

#A categorical columns into numerical (marital)
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder

df=pd.read_csv("D:\ExcelR\Python\Assignment\data_bank.csv")
df


df=df.iloc[:,:].values
df

m_status=LabelEncoder()
df[:,2]=m_status.fit_transform(df[:,2])
df

df=pd.DataFrame(df)
df

ct= ColumnTransformer(transformers=[('encode',OneHotEncoder(),[2])],remainder='passthrough')

df=ct.fit_transform(df)
df

df=pd.DataFrame(df)
df
#pd.get_dummies(df)


#B Rename all columns as df

df.rename(columns={0:'df1', 1:'df2', 2:'df3', 3:'df4',4:'df5', 5: 'df6',6:'df7',7:'df8',
                          8:'df9',9:'df10', 10:'df11',11:'df12',12:'df13', 
                          13:'df14',14:'df15', 15:'df16',16:'df17',17:'df18',18:'df19'})

df


#C rename only one column in df

df.rename(columns={4:'age'})
df.head()


#***************************************************************
#5. After doing all the changes in bank data(Q19). save the file in your directory in Csv Format.

import pandas as pd
import numpy as np

df.to_csv("bank.csv")

import os
os.getcwd()

#*****************************************************************************



# 1. Write Python Programs to use various operators in Python


#Airthmatic operations
a=5
b=10
print("Sum:", a+b)

print("sub:", a-b)

print("malt:", a*b)

print("Power:", b**a)

print("div:", a/b)

print("div2:", a//b)

print("mod:", a%b)



a=10
b=5

if a < b:
    print(" a smaller number")
else:
    print("a is bigger number")
    
if a > b:
    print("a is smaller number")
else:
    print("a is biggest number")
    
    
    
#Logical operators

a = 13
b = 33
  

print(a > b) 
  

print(a < b) 
  
# a == b is False 
print(a == b) 
  
# a != b is True 
print(a != b) 
  
# a >= b is False 
print(a >= b) 
  
# a <= b is True 
print(a <= b) 
        

#  2. Create list of elements and slice and dice it

colours=['red', 'green', 'black','blue','white','yellow']

colours[0]
colours[2]
colours[-1]
colours[-3]
colours[3]

colours.index('red')
colours.index('black')
colours.index("green")

colours[1:3]
colours[0:4]

#  3. Using while loop accept numbers until sum of numbers is less than 100

i= 10
while i<100:
    i=i+2
    print (i)
   

#  4. Write a python program Read & write Excel files 

import pandas as pd
import numpy as np


# write CSV file
std_data={"Name":["Rashmi","Ranjana","Bharath","Bahubali","Kavya","shruti"],
          "Age":[21,22,23,24,21,20],
          "Course":["BCA","BBA","Bcom","BCA","BCA","BBA"]}

df=pd.DataFrame(std_data)
df
df.columns

df.to_csv("students.csv")

import os
os.getcwd()

#read CSV file

df=pd.read_csv("D:\ExcelR\Python\Assignment\mtcars.csv") 
df


# 5.Write a python program to scrape reviews from a commercial web site

pip install beautifulsoup4 requests pandas


import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)
    
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()    
    
    
    
#********************
# 6. Create a 3x3 matrix with values ranging from 2 to 10 using numpy

import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)


#7. Write a Python program to convert a list of numeric value into a one-dimensional  
 #    NumPy array

import numpy as np

x=[6,5.5,2.023,200,0.45]
print("list:",x)

y=np.array(x)
print('One dimensional array:',y)



#8. Write a Python program to create a null vector of size 10 and update sixth value to 11.

import numpy as np
x = np.zeros(10)
print(x)

x[6] = 11
print("Update sixth value:",x)

