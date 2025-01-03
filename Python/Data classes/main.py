from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    profession: str

p = Person("Garima", 25, "Engineer")
print(p)


@dataclass
class Rectangle:
    width: int
    height: int
    color: str='white'


r1 = Rectangle(10, 20, 'blue')
r2 = Rectangle(15, 40, 'red')
print(r1)
print(r2)


@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(10, 20)

print(p.x, p.y)


# Inheritance

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    emp_id: int
    salary: float

p = Person("Garima", 25)
e = Employee("Garima", 25, 1001, 50000)

print(p)
print(e)


# Nested Dataclasses
@dataclass
class Address:
    city: str
    state: str
    pin: int

@dataclass
class Person:
    name: str
    age: int
    address: Address

add = Address("Delhi", "Delhi", 110001)
pr = Person("Garima", 25, add)

print(pr.address)
print(pr.address.city)