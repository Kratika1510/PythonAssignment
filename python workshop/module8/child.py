from automobile import *
import automobile

class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.doors=doors
        
    def set_doors(self,d):
        self.doors=d

    def get_doors(self):
        return self.doors

class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        Automobile.__init__(self,make,model,mileage,price)
        self.drive_type=drive_type

    def set_drive_type(self,dt):
        self.drive_type=dt

    def get_drive_type(self):
        return self.drive_type

class SUV(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        Automobile.__init__(self,make,model,mileage,price)
        self.pass_cap=pass_cap

    def set_pass_cap(self,s):
        self.pass_cap=s

    def get_pass_cap(self):
        return self.pass_cap

a=Car(20,"BMW","40kmph",20000000,200)
a.set_doors(200)
print(a.get_doors())
b=Truck(21,"mahindra","80kmph",3000000,100)
b.set_drive_type("basic")
print(b.get_drive_type())
c=SUV(32,"hyundai","60kmph",44556768,50)
c.set_pass_cap("pass")
print(c.get_pass_cap())

    
