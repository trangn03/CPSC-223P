# Name: Trang Ngo
# Date: 12/5/2022
# File Purpose: Tuffy Titan Vehicle management module 

class Vehicle:
    wheel_type = 'Tires'
    def __init__(self, color, engine_type):
        self.color = color
        self.engine_type = engine_type
        self.towing_capacity = 0

# Inherit from Vehicle
class Car (Vehicle):
    vehicle_classification = 'Car'
    def __init__(self, color, engine_type, passengers):
        super().__init__(color, engine_type)
        self.passengers = passengers

# Inherit from Vehicle
class Truck(Vehicle):
    vehicle_classification = 'Truck'
    def __init__(self, color, engine_type, passengers):
        super().__init__(color, engine_type)
        self.passengers = passengers

# Inherit from Car
class Sedan(Car):
    vehicle_type = 'Sedan'
    doors = 4

# Inherit from Car
class Coupe(Car):
    vehicle_type = 'Coupe'
    doors = 2

# Inherit from Truck
class Pickup(Truck):
    vehicle_type = 'Pickup'
    doors = 2

# Inherit from Truck
class SUV(Truck):
    vehicle_type = 'SUV'
    doors = 5