class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
        # self.engine = engine
        # self.make = make

class Work(Vehicle):
    def __init__(self, wheels,  additional_attri):
        super().__init__(wheels)
    
        self.additional_attri = additional_attri 

car1 = Work(55,6)
print(car1.additional_attri)