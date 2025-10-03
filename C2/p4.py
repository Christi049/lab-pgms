"""Python program that demonstrates both Pivot Tables and Cross Tabulations using the pandas library.
"""
import pandas as pd 

data = {
    'Student' : ['ALice','Bob','Alice','Henry'],
    'Marks' : [55,33,23,12],
    'Subject' : ['Math','Science','Science','Math'],
    'Class' : ['A','B','A','B']
}

df = pd.DataFrame(data)
print(df)

#pivot_table
pvt_table = pd.pivot_table(df,values='Marks',index='Class',columns='Subject',aggfunc = 'mean')
print(pvt_table)

#cross table
cross_table = pd.crosstab(df['Class'],df['Subject'])
print(cross_table)
