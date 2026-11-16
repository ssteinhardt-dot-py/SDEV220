class Solution:
    def firstSearch(self, arr, k):
        for key, value in enumerate(arr):
            if value == k:
                return key

class Vehicle():
    def __init__(self, vtype):
        self.vtype = vtype

class Automobile(Vehicle):
    def __init__(self, vtype, year, make, model, doors, roof):
        super().__init__(vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

year = input("Please enter the year: ")
make = input("Please enter the make: ")
model = input("Please enter the model: ")
doors = input("Please enter the number of doors: ")
roof = input("Please enter the type of roof: ")

car = Automobile("Car", year, make, model, doors, roof)
print("Vehicle type:", car.vtype)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("# of doors:", car.doors)
print("Type of roof:", car.roof)
