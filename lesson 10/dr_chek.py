import random as r
import datetime as d

while True:
    number = input("Скажи число (До 71)")
    if not number.isdigit()  or int(number) < 2:
        print(" BAN ")
        print("_" * 10)
    elif number == 71:
        print("ахахахахааахха ы нет")
        print("_" * 10)
    elif number == 1:
        print("ахахахахах дед инсайд")
        print("_" * 10)
    else:
        print("                              норм")
        number = int(number)
        break

birthdays = []
startofyear = d.date(2022, 1, 1)
for _ in range(number):
    shift = r.randint(0, 364)
    shiftofdays = d.timedelta(shift)
    birthday = startofyear + shiftofdays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays): #множества, повторения исключены
    if birthdays.count(i) > 1: # 2+ вхождения
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.")