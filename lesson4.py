# protected, private, public
# class Bank:


    # def __init__(self,name,age):
    #     self.name = name
    #     self._age = age
    #     self.__account = 0

    # def get_account(self):
    #     return self.__account
    #
    # def add_money(self,money):
    #     self.__account += money
    #     return self.__account

#     @property
#     def get_account(self):
#         return self.__account
#
#     @get_account.setter
#     def get_account(self, money):
#         if money >= 100000:
#             raise Exception("Too much money")
#
#         self.__account += money
#         return self.__account
#
# nazgul = Bank(age=26, name="Nazgul" )
# nazgul.get_account = 456789
# # nazgul = Bank(6778890, age=26, name="Nazgul" )
# nazgul._Bank__account = 456789
# print(nazgul._account)
# print(nazgul.__account)
# print(nazgul.name)
# print(dir(nazgul))
# print(nazgul._Bank__account)
# # print(nazgul.get_account())
# print(nazgul.add_money(10000))
# print(nazgul.get_account)
# nazgul.get_account = 68900
# print(nazgul.get_account)

# class Example:
#     var_a = 7
#     var_b = 100
#     def __init__(self,din_b):
#         self.din_a = 0
#         self.din_b = din_b
#
#     def set_din_a(self, a):
#         self.din_a = a
#         return self.din_a
#
#     def sum_(self):
#         return self.var_a + self.var_b
#
#     def power(self):
#         s = self.din_a ** self.din_b
#         t = self.din_b ** self.din_a
#         return s,t
#
# obj = Example(2)
# obj.set_din_a(3)
# print(obj.sum_())
# print(obj.power())

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         return self.a + self.b
#     def diff(self):
#         return self.a - self.b
#     def product(self):
#         return self.a * self.b
#     def division(self):
#         return self.a / self.b
# obj = Calculator(10,5)
# print(obj.sum())
# print(obj.diff())
# print(obj.product())
# print(obj.division())

class Hw:

    def __init__(self,a):
        self.a = a
        vowels = ['a', 'e', 'i', 'o', 'u']
    def func(a):
        if self.a.isalpha():
            for i in self.a:
                countv = 1
                countc = 1
                if i in vowels:
                    countv += 1
                    return countv
                else:
                    countc += 1
                    return countc

                    if countc*countv<=len(self.a):
                        return "vowels"
                    else:
                        return "consonants"

            return

        if self.a.isdigit():
            for i in self.a:
                count = 1
                if self.a %2 == 0:
                    count += 1
                    return count
                return count*len(self.a)

obj1 = Hw('length')
obj2 = Hw(45678)
print(obj1)
print(obj2)