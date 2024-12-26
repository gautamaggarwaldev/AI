import pandas as pd
import numpy as np

arr = np.arange(0,20).reshape(5,4)

df = pd.DataFrame(arr, index=["Row1", "Row2", "Row3", "Row4", "Row5"], columns=["Column1","Column2", "Column3", "Column4"])
print(type(df))
print(df)
print(df.head(2))
print(df.tail(2))

print(df.info())
print(df.describe())


# Indexing

print(df['Column1']) # series
print(df[['Column1', 'Column2', 'Column3']]) # dataFrame

print(df.loc['Row1']) # series
print(df.loc[['Row1', 'Row2', 'Row3']]) # dataFrames

print(df.iloc[2:4,0:2 ])
print(df.iloc[:, [0,-1]])

print(df.iloc[:, 0:].values)

print(df.isnull())

print(df['Column1'].value_counts())
print(df['Column1'].unique())

print(df[df['Column2']>2])