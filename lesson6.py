# #inheritance
# class Parent():
#
#     def work(self):
#         print("brings up child")
#
# class Child(Parent):
#     def play(self):
#         print("plays")
#     def work(self):
#         print("working 20 hours")
#
# child1 = Child()
# child1.play()
# child1.work()

# class Age:
#
#     def __init__(self,year):
#         self.year = year
#
#     def chinese_year(self):
#         return self.year * 3
#
#     def get_year(self):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - self.year
#
#     def get_info(self):
#         age = self.get_year()
#         print(f" age {age}, birth year {self.year}, height {self.height}")
#
# class NewAge(Age):
#     def __init__(self,year, height):
#         super().__init__(year)
#         self.height = height
#
#     def get_height(self,count_year):
#         current_year = self.year + count_year
#         twenty_five = self.height +4.7* 25
#         if count_year >= 25:
#             print(f" In  {current_year} your height {twenty_five} cm and no more height you will get")
#         else:
#             result = self.height +(4.7* count_year)
#             print(f" In  {current_year} your child height will be {result} cm")
#
#     def new_get_year(self):
#         # year_1 = Age().get_year(year)
#         year_1 = super().get_year()
#         return year_1 + 1
#
#
# ulan = Age(1998)
# ulan.get_info()
# kunduz = NewAge(1996,53)
# kunduz.get_info()
# print(kunduz.get_height(10))
# print(kunduz.get_year())
# print(kunduz.new_get_year())
# print(kunduz.chinese_year())
# nazgul = NewAge()
# print(nazgul.get_year(1996))
# print(nazgul.new_get_year(1996))
# print(nazgul.chinese_year(1996))


class Product:
    def __init__(self,name, price, mass):
        self.__name = name
        self.__price = price
        self.__mass = mass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
        return self.__price
    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        self.__mass = mass
        return self.__mass


class Buy(Product):
    def __init__(self, number,total_price,total_mass,name, price, mass):
        super().__init__(self, name, price, mass)
        self.number = number
        self.total_price =  total_price
        self.total_mass = total_mass

    def set_total_price(self):
        self.total_price = self.number * self.get_price()
        return self.total_price
    def set_total_mass(self):
        self.total_weight = self.number * self.get_mass()
        return self.total_mass

class Check(Buy):
    def get_info(self):
       print(f" name {self.get_name()}  number of product {self.number} total_price  {self.total_price} total_mass {self.total_mass}")

obj1 = Check("10","bread",25, 100,)
obj1.set_total_price(2)