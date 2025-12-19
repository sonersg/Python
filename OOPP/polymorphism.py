# Polymorphism
#
# The word polymorphism is derived from Greek and it means "having multiple forms".
#
# poly.. many
#
# morph.. forms
#
# We override the common methods in sub classes


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

    # def start(self):
    #     print("Car is starting..")
    #
    # def stop(self):
    #     print("Car is stoping..")


class Motorbike(Vehicle):
    def __init__(self, brand, model, year, brake_type):
        super().__init__(brand, model, year)
        self.brake_type = brake_type

    def start(self):
        print("Motorbike is starting..")

    def stop(self):
        print("Motorbike is stoping..")


car = Car("Honda", "Civic", 2022, "Su Motoru")
motorbike = Motorbike("Bisan", "Bisan", 2022, "Put ur feet on the ground.")

car.start()
motorbike.stop()
