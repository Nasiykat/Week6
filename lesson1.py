# datetime

import datetime
from datetime import timedelta

now = datetime.datetime.now()

# date_2 = datetime.date(2022, 5, 25)
# time_2 = datetime.time(13, 30)
# all_date = datetime.datetime.combine(date_2, time_2)
# print(date_2)
# print(time_2)
# print(all_date.strftime("%A"))
# print(now.strftime("%A"))


# days = 30
# end_date = now + timedelta(days)
# print(end_date)


# date_1 = datetime.date(2022, 6, 22)
# etap_1 = 30
# etap_2 = 20
# etap_3 = 50
# end_date = date_1 + timedelta(etap_1)
# end_date_1 = end_date + timedelta(etap_2)
# end_date_2 = end_date_1 + timedelta(etap_3)
# print("Конец первого этапа:", end_date)
# print("Конец второго этапа:", end_date_1)
# print("Конец третьего этапa:", end_date_2)



# year = int(input("Year: "))
# month = int(input("Month: "))
# day = int(input("Day: "))
# data = datetime.datetime(year, month, day)
#
# def devide_time(date):
#     stage1 = date + timedelta(30)
#     stage2 = stage1 + timedelta(20)
#     stage3 = stage2 + timedelta(50)
#     print(f"{stage1} конец первого этапа!")
#     print(f"{stage2} конец второго этапа!")
#     print(f"{stage3} защита!")
#     return stage1, stage2, stage3
#
# a = devide_time(data)
# print(a)



# lists = ["ps4", "dota", "ll", "warcraft"]
# def devide_time(renting, product):
#     now = datetime.datetime.now()
#     item_time = now + timedelta(renting)
#     print(f"{product} Должны возвратить {item_time}")
#     return {
#         f"{product}": item_time
#     }
#
# a = devide_time(2, lists[0])


#
# dt_string = "12/11/2018 09:15:32"
# dt_object1 = datetime.datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
# print("dt_object1 =", dt_object1)
#
# now = datetime.datetime.now()
# print(now.strftime("%d-%m-%Y %H:%M"))

#
# now = datetime.datetime.now()
# print(datetime.datetime.timestamp(now))
#
#
# timestamp = 300
# dt_object1 = datetime.datetime.fromtimestamp(timestamp)
# print(dt_object1)

def better_than_average(class_points, your_points):
    return class_points.append(your_points)
    print(class_points.append(your_points))
print(better_than_average([2,3,7], 5))


