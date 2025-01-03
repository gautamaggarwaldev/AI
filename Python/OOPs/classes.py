class Car:
    pass

car1 = Car()
car2 = Car()

car1.windows = 5
car1.doors = 4
car1.enginetype = "Petrol"

car2.windows = 3    
car2.doors = 2
car2.enginetype = "Diesel"

print(car1.enginetype) 
print(car2.enginetype)

print(dir(car1))