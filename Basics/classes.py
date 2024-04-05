

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Tesla", "Model 3")
print(my_car.make)
print(my_car.model)

my_bike = Vehicle("bisiklet", "mavi")
print(my_bike.make)
print(my_bike.model)

my_bike.get_make_model()



# INHERITANCE
class Airplane(Vehicle):
    def __init__(self, make, model, country):
        super().__init__(make, model)
        self.country = country

    def moves(self):
        print("Flies along...")

class GolfCart(Vehicle):
    pass

golf = GolfCart("golf", "cart2")
plane = Airplane("Uçak", "GT123", "Turkiye")
golf.get_make_model()
plane.get_make_model()
plane.moves()
print(plane.country)



# POLYMORPHISM
# The ability to behave differently to same input
for v in (my_car, my_bike, golf, plane):
    v.get_make_model()
    v.moves() 
