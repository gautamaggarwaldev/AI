import pandas as pd
from io import StringIO

df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
print(df.head())