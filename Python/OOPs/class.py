class Car:
    # constructor
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    
    def self_driving(self):
        print( "This is a {} car" .format(self.enginetype))


car1 = Car(4,4,"Petrol")

print("Doors {}" .format(car1.doors))
print("Windows {}" .format(car1.windows))

car1.self_driving()