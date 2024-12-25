print(type([]))

string = "garima"
print(string[2])
# string[2] = "h"  strings are immutable in python
print(string[2])


lst=[1,2,3,4,5,"string", "hello"]
print(lst)
lst[1] = "gg" # list is mutable
print(lst)

ll = list((1,2,3,4,5,6,7,8,9,8))
print(ll)

for i in ll:
    print(i+1)


print(max(ll))
print(min(ll))

ll.append(["james", "tony"])
print(ll[10])
print(ll)
print(ll[7:11])

ll.insert(2, "stark")
print(ll)

ll.extend(["james", "tony"])
print(ll)
print(ll*2)

ll.pop()
ll.pop(5)
print(ll)

print(ll.count(8))
print(len(ll))