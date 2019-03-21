class Vehicle:
    def __init__(self,wheels,weight):
        self.wheels=wheels
        self.weight=weight
    def display(self):
        print(self.wheels,self.weight)
class Car(Vehicle):
    def __init__(self,wheels,weight,passenger_load):
        super(Car,self).__init__(wheels,weight)
        self.passenger_load=passenger_load
    def displayCar(self):
        super(Car,self).display()
        print(self.passenger_load)
class Truck(Vehicle):
    def __init__(self,wheels,weight,passenger_load,payload):
        super(Truck,self).__init__(wheels,weight)
        self.passenger_load=passenger_load
        self.payload=payload
    def displayTruck(self):
        super(Truck,self).display()
        print(self.passenger_load,self.payload)
c=Car(4,2,5)
c.displayCar()
t=Truck(4,10,10,10)
t.displayTruck()

