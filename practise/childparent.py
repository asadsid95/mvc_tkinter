class Vehicle:

    colour = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed 
        self.mileage = mileage

    def fare(self, capacity):
        return capacity * 100

    # def seating_capacity(self, capacity):
    #     return f"seating capacity = {capacity}"

class Bus(Vehicle):

    def fare(self,capacity=50):
        return super().fare(capacity) * 1.1

    # def seating_capacity(self, capacity=50):
    #     return super().seating_capacity(500)
    

class Car(Vehicle):
    pass

school1_bus = Bus("Bus", 120, 12)
# print(school1_bus.seating_capacity(500))
school1_car = Car("Bus", 120, 12)

# print(school1_car.colour)
print(school1_bus.fare(50))
