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
calText += "\n"

weekSeparator = ("+----------" * 7) + "\n"
blankRow = ("|         " * 7) + "|\n"

currentDate = d.date(year, mouth, 1)

while currentDate.weekday() != 0: #пока не понедельник
    currentDate -= d.timedelta(days=1) #отнимаем 1 день

while True:
    calText += weekSeparator
    dayNamderRow = ""
    for i in range(7):
        dayNamderLabel = str(currentDate.day).rjast(2) #число
        dayNamderRow += "|" + dayNamderLabel + (" " * 7) #ряд(ячейка)
        currentDate += d.timedelta(days=1) #переход к след дню
    calText += "|\n"
    calText += dayNamderRow
    for i in range(3):
        calText += blankRow

    if currentDate.month != mouth:
        break

calText += weekSeparator
print(calText)

calendarFileName = 'calendar_{}_{}.txt'.format(mouth, year)
with open(calendarFileName, "w") as syperpudge:
    syperpudge.write(calText)

print('Сохранено в ' + calendarFileName)