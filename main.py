# # a = int(input("Число:"))
# # first = a // 100
# # second = (a // 10) % 10
# # tretie = a % 10
# # print("Последняя Цифра", a % 10)
# # print("Первая Цифра", a // 100)
# # print("Вторая Цифра", (a // 10) % 10)
# # print("Сумма цифр:", first + second + tretie)
# # print("Введи стоимость пирожка")
# # rub = int(input("Рублей:"))
# # cop = int(input("Копеек:"))
# # n = int(input("колличество:"))
# #
# # price_pie = rub * 100 + cop
# # all_money = price_pie * n
# #
# # print(f"С вас {all_money // 100}руб, и {all_money % 100}копеек")
# #
# # dengi = int(input("Ваши:"))
# # dengi = dengi * 100
# #
# # sdacha = dengi - all_money
# # sdacha = sdacha
# #
# # print(f"Ваша сдача: {sdacha // 100} рублей {sdacha % 100}копеек")
# a = int(input("a: "))
# if a % 2 == 1:
#     a = a + 1
# else:
#     a = a + 2
# print(a)
sec = int(input("sec: "))

m = (sec - 3600 * h) // 60
s = (sec - 3600 * h) - 60 * m

h = sec // 3600
if m >= 60:
    m = m - 60
    h = h + 1
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
if h < 10:
    h = "0" + str(h)
print(h, m, s)