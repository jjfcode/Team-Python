class Car:
    # class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def stop(self):
        if self.is_moving:
            print('The car has Stopped')
            self.is_moving = False
        else:
            print('The car has already stopped')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car start moving')
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

class Dealership:
    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)

car_one = Car("Ford Fusion", 2001)
car_two = Car("Mercedez c300", 2005)
car_three = Car("Mercedez c43", 2008)
my_dealership = Dealership()
my_dealership.add_car(car_one)
my_dealership.add_car(car_two)
my_dealership.add_car(car_three)
for car in my_dealership:
    print(car)

car_one = Car('Model T', 1908)
car_one.stop()
car_one.go('slow')
car_one.go('fast')
car_one.stop()
car_one.stop()
print(dir(car_one))
print(str(car_one))


car_two = Car('Phantom', 2020, 'Rolls Royce')
print(car_one.make)
print(car_two.make)
car_one.year = 2015
print(car_one.year)
print(car_two.year)






# print(car_one.doors)
# print(car_two.doors)
# print(Car.doors)

# car_one.doors = 4
# print(car_one.doors)
# print(car_two.doors)
# print(Car.doors)

# Car.doors = 5
# car_one.doors = 6
# print(f'car_one {car_one.doors}')
# print(id(car_one.doors))
# print(f'car_two {car_two.doors}')
# print(id(car_two.doors))
# print(f'Car {Car.doors}')
# print(id(Car.doors))