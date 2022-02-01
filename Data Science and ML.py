import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Construct a Multi-index level data frame
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

# Setting index names for the G1, and 1,2,3 layers
df.index.names = ['Groups', 'Num']
print(df)

# Grab value at G2, 2, Column B
print(df.loc['G2'].loc[2]['B'])

# Very useful function called 'Cross-Section'
print(df.xs(1, level='Num'))

'-----------------------------------------------------------------------'

# Missing Data
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# Explore the dropna method
df.dropna()
print(df)
# NOTE: dropna with axis 0 drops rows, and axis=1 drops columns with na values
df.dropna(axis=1)
print(df)
# NOTE: Thresh value will drop rows/columns with more than specified non-na values

# Explore the fillna method
print(df['A'].fillna(value=df['A'].mean()))

'-----------------------------------------------------------------------'

# Explore the groupby method to group rows of data together
# NOTE: Groupby allows you to group together rows based off of a column
# and perform an aggregate function on them

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Midi', 'Sue', 'Cole', 'Jen', 'Schmegan', 'Luxi'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)

byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum())
print(byComp.std())

# Won't usually create a groupby variable, but will instead do a one-liner
print(df.groupby('Company').sum().loc['GOOG'])

# Using the describe method to give lots of useful information
print(df.groupby('Company').describe())
# If you don't prefer the output format, use .transpose to change it
print(df.groupby('Company').describe().transpose())

'-----------------------------------------------------------------------'

# Learning Merging, Joining, and Concatenating data frames

# Concatenation essentially glues together dataframes. Keep in mind that
# dimensions should match along the axis you are concatenating on.
# You can use pd.concat and pass in a list of DFs to concatenate together
# Example: pd.concat([df1, df2, df3])

# Pandas is capable of using the merge function to do merge logic.
# It's very similar to merging SQL tables together.
# Using the pd.merge function, you can merge DFs together.
# Example: pd.merge(df1, df2, how='inner', on='key')

# Joining is a convenient method for combining the columns of two
# potentially differently-indexed DFs into a single resulting DF.
# You can think of this as the same thing as merge, except the keys you
# want to join on are on your index instead of a column.

'-----------------------------------------------------------------------'

# Learning about operations
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [222, 444, 666, 222],
                   'col3': ['abc', 'def', 'ghi', 'jkl']})

print(df.head())

# There are three main useful methods concerned with finding unique values in a data frame.
# If you want to find all unique values in a column, you can use the .unique() method.
print(df['col2'].unique())

# NOTE: .unique() method returns a list of all unique values. If you want the number of unique values,
# use .nunique() method, and it will return the total of unique values.

# If you want a table of the unique values AND how many times they show up, use the value_counts() method
print(df['col2'].value_counts())


# Exploring the .apply() method which allows you to apply a function to pandas DFs.
# Consider the following function:


def times2(x):
    return x * 2


print(df['col2'].apply(times2))

# .apply() method is especially powerful when combined with lambda expressions. Example for the prior
# function that was defined.
print(df['col2'].apply(lambda x: x * 2))

# To delete a column, use the .drop() method. NOTE: changes made won't affect original DF unless you set
# inplace == True.
print(df.drop('col1', axis=1))
print(df)

# You can use the df.columns() method to figure out what the names of each column is.
print(df.columns)

# Use the .sort_values() method to sort the data by specific column
print(df.sort_values('col2'))

# You can use the isnull() method to find null values. For this specific example, there will be none.
print(df.isnull())

# Exploring pivot tables
# Creating new dataframe
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 2, 3, 4, 3, 2]}

df = pd.DataFrame(data)
print(df)

# Use the pivot_table() method to create a pivot table out of the select DF.
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))

'-----------------------------------------------------------------------'

# Explore reading and writing files with pandas.
# Use the .read_csv() method to read a csv file
print(pd.read_csv('example.csv'))

# To write to a csv, you must first create a df of the csv file.
df = pd.read_csv('example.csv')
print(df)

# Use .to_csv() method to write to a csv file. Use index=False to get rid of old index.
df.to_csv('Output.csv', index=False)

# To read from excel files, you need to use the .read_excel() method and pass in the
# xlsx file name, and the sheet name of the data within the excel file itself.
# Example: pd.read_excel('Excel_Sample.xlsx', sheetname='Sheet1')

# To write to an excel file, it's the same process as writing to a csv. You must create
# a DF, then use the .to_excel() method to write it.
# Example: df.to_excel('Excel_Sample2.xlsx', sheet_name='Sheet1')

# To read from an HTML website, store the following into a variable and use .read_html() method.
# Example: data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

'-----------------------------------------------------------------------'

# Learning MatPlotLib
# Create some data to graph
x = np.linspace(0, 5, 11)
y = x ** 2

# Creating a graph using the functional method with matplotlib.
# NOTE: When you want to show the graph, remember to use the plt.show() line.
plt.plot(x, y)

# Adding titles and labels to the graph.
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Data')

# Putting multi-plots on the same canvas
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')

# Creating graphs using the object-oriented method (much better) method with matplotlib.
# The main idea with OO method is to create figure objects and then call methods off of this.
# First, create an object. Imagine it's your blank canvas.
fig = plt.figure()
# Now add Axes to the object. Takes in a list of 4 arguements: Left, bottom, width, and height
# that range from 0 to 1. Basically the % of the blank canvas you want to make.
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('X Axis')
axes.set_ylabel('Y Axis')
axes.set_title('Data of X and Y')

# Plotting another set of data within the same canvas.
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes2.plot(y, x)

# Add titles to the separate plots
axes1.set_title('Data X Y')
axes2.set_title('Data Y X')

# Creating subplots using the same OO programming
# NOTE: if more rows and cols of graphs, say 3 and 3, you can use plt.tight_layout() method to get rid of overlap.
# In this case, 'axes' is an list type, meaning you can iterate through them.
fig, axes = plt.subplots(nrows=1, ncols=2)

# for current_ax in axes:
#     current_ax.plot(x, y)

# Since you can iterate through the subplots, you may also index it.
axes[0].plot(x, y)
axes[0].set_title('First plot')

axes[1].plot(y, x)
axes[1].set_title('Second plot')

# Exploring figure size, aspect ratio, and DPI
fig2 = plt.figure(figsize=(3, 2))
ax = fig2.add_axes([.1, .1, 1, 1])
ax.plot(x, y)

plt.show()
