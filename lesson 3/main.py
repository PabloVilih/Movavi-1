# # # # # # # # a = int(input("Число:"))
# # # # # # # # first = a // 100
# # # # # # # # second = (a // 10) % 10
# # # # # # # # tretie = a % 10
# # # # # # # # print("Последняя Цифра", a % 10)
# # # # # # # # print("Первая Цифра", a // 100)
# # # # # # # # print("Вторая Цифра", (a // 10) % 10)
# # # # # # # # print("Сумма цифр:", first + second + tretie)
# # # # # # # # print("Введи стоимость пирожка")
# # # # # # # # rub = int(input("Рублей:"))
# # # # # # # # cop = int(input("Копеек:"))
# # # # # # # # n = int(input("колличество:"))
# # # # # # # #
# # # # # # # # price_pie = rub * 100 + cop
# # # # # # # # all_money = price_pie * n
# # # # # # # #
# # # # # # # # print(f"С вас {all_money // 100}руб, и {all_money % 100}копеек")
# # # # # # # #
# # # # # # # # dengi = int(input("Ваши:"))
# # # # # # # # dengi = dengi * 100
# # # # # # # #
# # # # # # # # sdacha = dengi - all_money
# # # # # # # # sdacha = sdacha
# # # # # # # #
# # # # # # # # print(f"Ваша сдача: {sdacha // 100} рублей {sdacha % 100}копеек")
# # # # # # # a = int(input("a: "))
# # # # # # # if a % 2 == 1:
# # # # # # #     a = a + 1
# # # # # # # else:
# # # # # # #     a = a + 2
# # # # # # # print(a)
# # # # # # sec = int(input("sec: "))
# # # # # #
# # # # # # m = (sec - 3600 * h) // 60
# # # # # # s = (sec - 3600 * h) - 60 * m
# # # # # #
# # # # # # h = sec // 3600
# # # # # # if m >= 60:
# # # # # #     m = m - 60
# # # # # #     h = h + 1
# # # # # #     m = "0" + str(m)
# # # # # # if s < 10:
# # # # # #     s = "0" + str(s)
# # # # # # if h < 10:
# # # # # #     h = "0" + str(h)
# # # # # # print(h, m, s)
# # # # #
# # # # # temp = x[-1]
# # # # x = input("Введи что-то")
# # # # temp = x[-1]
# # # # print(x.index(temp) + 1)
# # # #
# # # # # print(len(x))
# # # # name_1 = "Антон"
# # # # name_2 = "Вова"
# # # # name_3 = "Бадан"
# # # #
# # # # bratva = [name_1, name_2, name_3]
# # # # print(bratva)
# # # # print(bratva[0][2:])  #bratva[0] - Антон, [2:] срез до конца строки
# # #
# # # path = "С:/Python3/python.exe"
# # # temp = path.split("/")
# # # print("Имя файла:", temp[-1])
# # # print("Расширение:", temp[-1][-3:])
# # # print("Имя каталога:", temp[1])
# # # print("Полный путь к каталогу:", temp[0] + "/" + temp[1])
# # chapter_1 = input("Глава 1: ")
# # page_1 = input("Страница: ")
# #
# # chapter_2 = input("Глава 2: ")
# # page_2 = input("Страница: ")
# #
# # chapter_3 = input("Глава 3: ")
# # page_3 = input("Страница: ")
# # print(chapter_1.ljust(15), page_1.rjust(15))
# # print(chapter_2.ljust(15), page_2.rjust(15))
# # print(chapter_3.ljust(15), page_3.rjust(15))
# x = "123456789"
# print(x[::2])  #через одно число
# print(x[::-1])  #в обратном порядке
# print(x[::-2])  #в обратном порядке через одно число
# x = "12'345'678"
# Решение 1 через срез
# temp = x[:2] + x[3:5] + x[-3:]
# number = int(temp)
# print(number)

# Решение 2 через .split()
# temp = x.split("'")
# temp2 = temp[0] + temp[1] + temp[2]
# number = int(temp2)
# print(number)

# Решение 3 через .replace()
# temp = x.replace("'", "")
# number = temp
# print(number)