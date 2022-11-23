import datetime as d

MONTHS = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
DAYS = ("Понедельник", "Вторник", "Среда Четверг", "Пятница", "Суббота", "Воскресенье")

while True:
    year = input("Год: ")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break

while True:
    mouth = input("Месяц: ")
    if mouth.isdigit() and int(mouth) > 0:
        mouth = int(mouth)
        break

calText = ""
calText += (" " * 34) + MONTHS[mouth - 1] + " " + str(year) + "\n"

for i in range(7):
    calText += DAYS[i] + " "

print(calText)
weekSeparator = ("+----------" * 7) + "\n"
blankRow = ("          " * 7) + "|\n"