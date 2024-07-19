#PRINT STATEMENT IS NECESSARY TO GET OUTPUT IN THE TERMINAL
import pandas as pd
dict_of_students = {'Student':['David','Samuel','Terry','Evan'], 
                   'Age':['27','24','22','32'],
                   'Country':['Uk','Canada','China','USA'],
                   'Course':['Python','Data Structures','Machine Learning','Web Development'],
                   'Marks':['85','72','89','76']}
df1= pd.DataFrame(dict_of_students)
df1

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

z = df1[['Marks']]
z

c = df1[['Country','Course']]
c

x = df1['Student']
x

#check the type of x
type(x)

#Exercise 2: loc() and iloc() functions

# Access the value on the first row and the first column

df.iloc[0, 0]


# Access the column using the name

df.loc[0, 'Salary']

df2=df
df2=df2.set_index("Name")

#To display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']

# Write your code below and press Shift+Enter to execute
print(df.loc[2:3,'Name':'Department'])  

