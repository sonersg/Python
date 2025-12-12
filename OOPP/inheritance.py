# Inheriitance
#
# A car is a vehicle
# A bike is a vehicle
#
# Vehicle --> Base or super class
# Car, Bike --> Sub classes


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting..")

    def stop(self):
        print("Vehicle is stoping..")


class Car(Vehicle):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self.engine_type = engine_type


class Bike(Vehicle):
    def __init__(self, brand, model, year, brake_type):
        super().__init__(brand, model, year)
        self.brake_type = brake_type


car = Car("Honda", "Civic", 2022, "Su Motoru")
bike = Bike("Bisan", "Bisan", 2022, "Put ur foot on the wheel")
print(bike.__dict__)
print(car.__dict__)
car.start()
bike.stop()
