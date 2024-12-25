# Sets

print(type({1,2,3,4,5,6}))
print({1,2,3,4,5,6})

print(set([1,2,3,4,5,5]))

set_var = {"tony", "thor", "CA"}
print(set_var)
# print(set_var[1]) set object is not subscriptable

for i in set_var:
    print(i)


set_var.add('hulk')
print(set_var)

set1 = {"ironman", "thor", "hulk"}
set2 = {"ironman", "thor", "hulk", "antman"}

print(set2.intersection(set1))
set2.intersection_update(set1)
print(set2)
set2 = {"ironman", "thor", "hulk", "antman"}

print(set2.difference(set1))

print(set2.issuperset(set1))
print(set1.issubset(set2))


# Dictionary

print(type({}))

print({1 : "KK"})

print(dict(name="GG", age=145))


dit = {"c1":"audi", "c2":"bmw", "c3":"maybach", "c4":"nano"}

print(dit["c2"])

print(dit.items())

for i in dit.values():
    print(i)

dit["c5"]="swift"
print(dit)

# tuples

mytuple = ("gg","hello","world")
print(mytuple)
print(type(mytuple))

print(mytuple.count('hello'))
print(mytuple.index('gg'))