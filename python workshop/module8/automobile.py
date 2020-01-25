class Automobile():
        def __init__(self,make,model,mileage,price):
            self.make = make
            self.model=model
            self.mileage=mileage
            self.price=price

        def set_make(self,m):
            self.make = m

        def set_model(self,n):
            self.model=n

        def set_mileage(self,k):
            self.mileage=k

        def set_price(self,p):
            self.price=p

        def get_make(self):
            return self.make

        def get_model(self):
            return self.model

        def get_mileage(self):
            return self.mileage

        def get_price(self):
            return self.price

a=Automobile(20,"Alto","20kmph",200000)
a.set_make(56)
a.set_model("Alto")
a.set_mileage("20kmph")
a.set_price(200000)
print(a.get_make())
print(a.get_model())




