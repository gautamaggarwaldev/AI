### Access Modifier--->Encapsulation
## private

class Person:
    ## constructor
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display_info(self):
        print(f"the person name is {self.__name} and the age is {self.__age}")


person=Person("Garima",32)

person.display_info()


### Access Modifier--->Encapsulation
## Protected 

class Person:
    ## constructor
    def __init__(self,name,age):
        self._name=name
        self._age=age


person=Person("Garima",32)
print(dir(person))
print(person._age)


class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def display_info(self):
        print(f"the person name is {self._name} and the age is {self._age}")


student1=Student("Krish",33)
student1.display_info()