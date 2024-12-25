# if statement

# val = input("enter the number ")
val = 15
val_float = float(val)
if val_float > 100:
    print("hello")
else:
    print("world")

# nested else if

if val_float < 18:
    print("minor")
elif val_float > 18 and val_float < 56:
    print("young")
else:
    print("old")

# loops

lst = [1, 2, 3, 4, 6, 8]
for i in lst:
    print(i)


lst = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in lst:
    sum += i

print(sum)

# while loop

i = 0
while i <= 10:
    print(i)
    i += 1


# break

x=1
while(x<=7):
    print(x)
    if(x==4):
        break
    x+=1


# continue
x=1
while(x<=7):
    x+=1
    if(x==4):
        continue
    print(x)

