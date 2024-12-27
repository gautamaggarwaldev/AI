import pandas as pd
from io import StringIO

df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
# print(df.head())

data =('col1,col2,col3\n' 'x,y,1\n' 'a,b,2\n' 'c,d,3')

print(type(data))

# in memory file format object
print(StringIO(data))
print(pd.read_csv(StringIO(data)))
print(pd.read_csv(StringIO(data),usecols=['col1','col2']))

df.to_csv('test.csv',index=False) # save to csv file


# datatype in csv

data = ('a,b,c,d\n' '1,2,3,4\n' '5,6,7,8\n' '9,10,11')
df = pd.read_csv(StringIO(data))
print(df)
print(df.info())
df = pd.read_csv(StringIO(data),dtype=object)
print(df.info())

print(df.isnull().sum())

print(df['a'][0])


df = pd.read_csv(StringIO(data),dtype={'a':int,'b':float,'c':'Int64'})
print(df.info())
print(df.dtypes)

data = ('a,b,c\n' '4,apple,bat\n' '8,orange,cow')

df = pd.read_csv(StringIO(data),index_col=0)
print(df)

# use index cols and usecols
df = pd.read_csv(StringIO(data),index_col=0,usecols=['a','b','c'])
print(df)

# print(pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t'))





df = pd.read_csv("V:\AI Engineer Series (AES)\cu.item", sep='\t')
print(df)


