# class ItSchool:
#     bootcamp = 15000
#     time = "8.30"

# kunduz = ItSchool()
# yasir = ItSchool()
# aliya = ItSchool()
# yasir.bootcamp = 16000
# yasir.free = True
# # print(kunduz.bootcamp)
# # print(dir(kunduz))
# # print(kunduz.time)
# # print(kunduz.__dict__)
# # print(ItSchool.__dict__)
# print(yasir.__dict__)
# print()
# print(aliya.__dict__)

# class CarCarolla:
#     wheels = 4
#     volume = 1.8
#     engine = "v6"
#     kuzov = "sedan"
#
#     def __init__(self, bumper, color, otdelka):
#         self.bumper = bumper
#         self.color = color
#         self.otdelka = otdelka
#
#     def get_info(self):
#         print(f"{self.bumper},  color of car :{self.color},"
#               f" otdelka mashin {self.otdelka}")
#
#     def change_otdelka(self,new_otdelka):
#         self.otdelka = new_otdelka
#
#     def get_hello(self):
#         print("hello world")
#
#
#
# mirlan = CarCarolla("m obves","white","alcantaro")
# andrei = CarCarolla("v obves","green","crocodile")
# mirlan.get_info()
# mirlan.change_otdelka("alpaka")

# print(mirlan.__dict__)
# print(andrei.__dict__)
# print(mirlan.bumper)
# print(mirlan.engine)
# mirlan.get_hello()


# lessons_timur = {
#     "variables": 100,
#     "loop": 87,
#     "func": 58,
# }
# lessons_nasiykat = {
#     "variables": 100,
#     "loop": 90,
#     "func": 79,
# }
# lessons_aliya = {
#     "variables": 100,
#     "loop": 78,
#     "func": 98,
# }
#
# class Student:
#     group = "python_bootcamp_8:30"
#
#     def __init__(self, full_name, age, phone_number, lesson):
#         self.full_name = full_name
#         self.age = age
#         self.phone_number = phone_number
#         self.lesson = lesson
#         self.avg = 0
#
#     def get_info(self):
#         print(f" group {self.group} Zovut {self.full_name} age: {self.age}"
#             f"phone number: {self.phone_number} lesson:{self.lesson}  avg: {self.avg}")
#
#     def set_avg(self):
#         result = sum(self.lesson.values()) / len(self.lesson)
#         self.avg = int(result)
#
#     def set_avg_2(self):
#         count = 0
#         for i in self.lesson.values():
#             count +=i
#         self.avg = round(count/len(self.lesson))
#         # print(self.avg)
#
#
# timur = Student("Nasirdinov Timur",18,"+996773456789",lessons_timur)
# nasiykat = Student("Arzybaeva Nasiykat",38,"+996773189252",lessons_nasiykat)
# aliya = Student("Narynbekova Aliya",21,"+996773769800",lessons_aliya)
# # timur.get_info()
# # timur.set_avg()
# # timur.get_info()
# # nasiykat.get_info()
# aliya.get_info()
# aliya.set_avg_2()
# aliya.get_info()

# def yell(text: str):
#     return text.upper()+"!"
# print(yell("hello"))

# shout = yell
# print(shout("hey, come!"))
# def greet(func):
#     result = func("hello")
#     return result
# print(greet(yell))
#
# def speak(text):
#     def whisper():
#         return text.lower()+"...."
#     # result = whisper()
#     return whisper()
# print(speak("HELLO"))

# def speak(volume):
#     def whisper(text):
#         return text.lower()
#     def shout(text):
#         return text.upper()
#
#     if volume>5:
#         return shout
#     else:
#         return whisper
#
# result = speak(4)
# print(result("i am fine"))

# def make_adder(x):
#     def add(n):
#         return x+n
#     return add
# plus_3 = make_adder(3)
#
# print(plus_3(34))
# print(plus_3(23))

def count_positives_sum_negatives(arr):
    result = []
    for i in arr:
        count_p = 0
        count_n = 0
        if i > 0:
            count_p += 1
        result.append(count_p)
        if i < 0:
            count_n += i
        result.append(count_n)
    return result
print(count_positives_sum_negatives([1,2,3,-6,-3]))
