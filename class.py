# Assignment 1: Superhero Class
class Superhero:
    def __init__(self, name, power, origin, weakness):
        self.name = name
        self.power = power
        self.origin = origin
        self.weakness = weakness

    def introduce(self):
        return f"I am {self.name}, and I have the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}! 💪🏾"

    def use_weakness(self):
        return f"{self.name}s' weakness is {self.weakness}! ⚠️"
# Inheritance: A Flying Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, weakness, flight_speed):
        super().__init__(name, power, origin, weakness)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h! 🦸‍♂️"

# Creating a Superhero instance
superman = FlyingSuperhero("Superman", "Super Strength", "Krypton", "Kryptonite", 500)

# Output
print(superman.introduce())
print(superman.use_power())
print(superman.use_weakness())
print(superman.fly())

print("\n" + "="*40 + "\n")  # Separator for clarity on which assignment is which

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # This will be overridden by subclasses

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Creating instances
car = Car()
plane = Plane()
boat = Boat()

# Using polymorphism
vehicles = [car, plane, boat]

for vehicle in vehicles:
    print(vehicle.move())
