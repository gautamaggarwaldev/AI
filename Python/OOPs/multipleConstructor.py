'''
    class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __init__(self, name):
            self.name = name

    dog = Animal("Dog",45)

    print(dog)
'''

class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.color = args[2]
    
    def make_sound(self, sound):
        print("Dog makes sound {}" .format(sound))


dog=Animal("Dog", 45, "Brown")
print(dog.name)
print(dog.age)
print(dog.color)
dog.make_sound("Bark")