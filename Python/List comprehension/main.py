# List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
lst = [1,2,3,4,5,6]
newLst = [i**2 for i in lst]
print(newLst)

# list comprehension with if statement
number = [1,2,3,4,5,6,7,8,9,10]
even = [n for n in number if n%2==0]
odd = [n for n in number if n%2!=0]

print(even)
print(odd)

# nested list comprehension

lst = [[1,2,3],[4,5,6],[7,8,9]]
fl = [j for i in lst for j in i]
print(fl)

# Generating a list of the first letters of words in a list:
words = ['apple', 'banana', 'cherry', 'date']
first_letters=[word[0] for word in words]
print(first_letters)

# Generating a list of the squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[n**2 for n in numbers if n%2==0]

## Converting a list of strings to a list of integers
strings = ['1', '2', '3', '4', '5']
[int(s) for s in strings]

## Generating a list of the Fibonacci sequence using a list comprehension
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
fidLst = [fib[i-1] + fib[i-2] for i in range(2, len(fib))]
print(fidLst)

##Generating a list of all the divisors of a number:

number =36
lst = [i for i in range(1,number+1) if number%i==0]
print(lst)