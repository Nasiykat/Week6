#
# class Example:
#
#     def func(self, arg):
#         if isinstance(arg, str):
#             if sum(x in "ауоыиэюяеё" for x in arg.lower()) * sum(
#                     x in "бвгджзйклмнпрстфхцчшщ" for x in arg.lower()) <= len(arg):
#                 return ''.join([x for x in arg if x.lower() in "ауоыиэюяеё"])
#             else:
#                 return ''.join([x for x in arg if x.lower() in "бвгджзйклмнпрстфхцчшщ"])
#         elif isinstance(arg, int):
#             return sum(int(x) for x in str(arg) if x in "2468") * self.func_2(arg)
#
#     def func_2(self, arg):
#         return len(str(arg))
#
#
# obj = Example()
# test_case_1 = obj.func("Привет дружище! Как дела?")
# test_case_2 = obj.func("Что-то давненько тебя не видел.")
# test_case_3 = obj.func(123)
# test_case_4 = obj.func("иду")
#
# # print(test_case_1)
# # print(test_case_2)
# # print(test_case_3)
# print(test_case_4)


# class Example:
#
#     def func(self, arg):
#         if isinstance(arg, str):
#             if sum(x in "aeiou" for x in arg.lower()) * sum(
#                     x in "bcdfghjklmnpqrstvwxyz" for x in arg.lower()) <= len(arg):
#                 return ''.join([x for x in arg if x.lower() in "aeiou"])
#             else:
#                 return ''.join([x for x in arg if x.lower() in "bcdfghjklmnpqrstvwxyz"])
#         elif isinstance(arg, int):
#             return sum(int(x) for x in str(arg) if x in "2468") * self.func_2(arg)
#
#     def func_2(self, arg):
#         return len(str(arg))
#
#
# obj = Example()
# test_case_1 = obj.func("i am hardworking")
# test_case_2 = obj.func(" Life is pretty")
# test_case_3 = obj.func(236)
# test_case_4 = obj.func("may")
#
# print(test_case_1)
# print(test_case_2)
# print(test_case_3)
# print(test_case_4)

class Product:
    __name = None
    __price = None
    __weight = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Buy(Product):
    def __init__(self):
        self.__number = None
        # self.__total_price = None
        # self.__total_weight = None

    def set_total_price(self):
        self.total_price = self.number * self.get_price()
        return self.total_price

    def set_kol(self, number):
        self.number = number
        return self.number

    def set_total_weight(self):
        self.total_weight = self.number * self.get_weight()
        return self.total_weight

class Check(Buy):

    def get_info(self):
        print(f"name {self.get_name()}, number {self.number}, total_price {self.set_total_price()}, total_weight {self.set_total_weight()}")


obj1 = Check()
obj1.set_name("bread")
obj1.set_price(30)
obj1.set_kol(3)
obj1.set_weight(3)
obj1.get_info()


