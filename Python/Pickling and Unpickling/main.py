import seaborn as sns
import pickle

df = sns.load_dataset('iris')
print(df.head())

filename = 'iris.pkl'

# serialize
pickle.dump(df, open(filename, 'wb'))

# deserialize
print(pickle.load(open(filename, 'rb')))

example = {'fn':'gg', 'ln':'ag'}

pickle.dump(example, open('example.pkl', 'wb'))
print(pickle.load(open('example.pkl', 'rb')))

