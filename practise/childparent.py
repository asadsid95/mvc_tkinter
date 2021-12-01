class Vehicle:
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine
        # self.make = make

# This extends parent's functionality by adding more attributes
class Work(Vehicle):
    def __init__(self, wheels, engine,emergency_phone):
        super().__init__(wheels, engine)
    
        self.emergency_phone= emergency_phone 

# Here, parent's functionality is NOT extended; It simply inherit all from parent and 
class Personal(Vehicle):
    pass

car1 = Work(4, 3.5, True)
print('Work vehicle''s wheels:', car1.wheels)

car2 = Personal(6, 6.3)
print('Personal vehicle''s wheels:', car2.wheels)