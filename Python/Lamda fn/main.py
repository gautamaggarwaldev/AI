f = lambda x,y: x+y
print(f)
print(f(5,6))

## Return the length of a string
string_length=lambda s:len(s)
str = string_length("Garima KK")
print(str)

## Convert a list of integers to their corresponding square values:
numbers=[1,2,3,4,5,6]
squares=list(map(lambda x:x**2,numbers))
print(squares)

## Filter out even numbers from a list:

numbers=[1,2,3,4,5,6]
even = list(filter(lambda x:x%2==0,numbers))
print(even)

f=lambda x:x%2==0
print(f(3))


## Sort a list of strings based on their alphabetical characters and  length:
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
f = sorted(fruits,key=lambda x:len(x))
print(f)

## complex examples
## Sorting a list of dictionaries based on a specific key
people = [
    {'name': 'Alice', 'age': 25, 'occupation': 'Engineer'},
    {'name': 'Bob', 'age': 30, 'occupation': 'Manager'},
    {'name': 'Charlie', 'age': 22, 'occupation': 'Intern'},
    {'name': 'Dave', 'age': 27, 'occupation': 'Designer'},
]
ans = sorted(people,key=lambda x:(x['age']))
print(ans)

## Finding the maximum value in a dictionary
data = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
x = max(data,key=lambda x:data[x])
print(x)

## Grouping a list of strings based on their first letter
from itertools import groupby

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

groups = groupby(sorted(words), key=lambda x: x[0])

for key, group in groups:
    print(key, list(group))