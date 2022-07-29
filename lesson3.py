class Car:
    wheels = 4

    def __init__(self,model,color,owner,year):
        self.model = model
        self.miles = 0
        self.fuel_tank = 0
        self.color = color
        self.owner = owner
        self.year = year

    def get_fuel_tank(self, litre):
        self.fuel_tank += litre
        print(f"You filled {litre} of fuel,so finally you have {self.fuel_tank} litres in your tank")
        return self.fuel_tank

    def drive(self, km):
        litre = km * 0.1
        if self.fuel_tank >= litre:
            print("we may drive")
            self.miles += km
            self.fuel_tank -= litre
        else:
            print("You are lack of fuel!")


    def change_color(self, new_color):
        self.color = new_color
        print(f"Welcome your new color {self.color}")


tesla = Car("Model X", "white","Nasiykat","2022")
porshe = Car("Model Y", "silver","Kairat","2022")
tesla.get_fuel_tank(40)
tesla.change_color("green")
tesla.wheels = 6
del tesla.wheels
porshe.ceiling = open
# tesla.get_fuel_tank(50)
# porshe.get_fuel_tank(30)
# tesla.drive(400)
# porshe.drive(800)
# print(tesla.fuel_tank)
# print(porshe.fuel_tank)
# print(tesla.color)
# print(tesla.wheels)
# print(tesla.__dict__)
print(porshe.__dict__)
