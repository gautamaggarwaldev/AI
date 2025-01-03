def PrintHello():
    print("Hello World")


PrintHello()
PrintHello()
PrintHello()

def evenOddSum(lst):
    evenSum = 0
    oddSum = 0
    for i in lst:
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    return evenSum, oddSum

print(evenOddSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))