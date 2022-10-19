# # # # # # # # # # x = 7
# # # # # # # # # # # if x < 7 or x == 7:
# # # # # # # # # # #     print("menche libo ravno")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("bolshe")
# # # # # # # # # #
# # # # # # # # # # if x <= 7:
# # # # # # # # # #     print("menche libo ravno")
# # # # # # # # # # else:
# # # # # # # # # #     print("bolshe")
# # # # # # # # # #         # <=  меньше либо равно
# # # # # # # # # x = 7
# # # # # # # # #
# # # # # # # # # print(x == 7)
# # # # # # # # # print(x < 7)
# # # # # # # # x = int(input("vvedi chislo: "))
# # # # # # # # if x < 0:
# # # # # # # #     print("otricatelnoe")
# # # # # # # # elif
# # # # # # # year = int(input("vvedi god: "))
# # # # # # # if year % 4 == 0 and (year % 400 == 0 or year )
# # # # # # number_1 = int(input("pervoe chislo"))
# # # # # # operation = input("vvedi operaciu (+, -, *, /): ")
# # # # # # number_2 = int(input("vtoroe chislo"))
# # # # # #
# # # # # # lst = ["+", "-", "*", "/" ]  # список возможных операций
# # # # # # if operation in lst: # если операция возможна
# # # # # #     if operation == "+": #
# # # # # #         print(number_1 + number_2)
# # # # # #     elif operation == "-": #
# # # # # #         print(number_1 - number_2)
# # # # # #     elif operation == "/": #
# # # # # #         print(number_1 / number_2)
# # # # # #     else:
# # # # # #         print(number_1 * number_2)
# # # # # # else:
# # # # # #     print("ychi yroki mchk frede")
# # # # # # number_1 = int(input("pervoe chislo"))
# # # # # # number_2 = int(input("vtoroe chislo"))
# # # # # # number_3 = int(input("tretie chislo"))
# # # # # # count_pol = 0
# # # # # # count_otr = 0
# # # # # #
# # # # # # if number_1 > 0:
# # # # # #     count_pol += 1
# # # # # # elif number_1 < 0:
# # # # # #     count_otr += 1
# # # # # #
# # # # # # if number_2 > 0:
# # # # # #     count_pol += 1
# # # # # # elif number_2 < 0:
# # # # # #     count_otr += 1
# # # # # #
# # # # # # if number_3 > 0:
# # # # # #     count_pol += 1
# # # # # # elif number_3 < 0:
# # # # # #     count_otr += 1
# # # # # #
# # # # # # print("Polozitelnix", count_pol)
# # # # # # print("Otricatelnix", count_otr)
# # # # # number_1 = int(input("pervoe chislo"))
# # # # # number_2 = int(input("vtoroe chislo"))
# # # # # number_3 = int(input("tretie chislo"))
# # # # # lst = [number_1, number_2, number_3]
# # # # # min = min(lst)
# # # # # max = max(lst)
# # # # #
# # # # # print("samoe bolshoe:", max)
# # # # # print("samoe malenkoe:", min)
# # # #
# # # # h = int(input("chasi:"))
# # # # m = int(input("minyti:"))
# # # # s = int(input("sikynd:"))
# # # #
# # # # if (h > 23 or h < 0) or (m > 59 or m < 0) or (s > 59 or s < 0):
# # # #     print("format neverniy :(")
# # # # else:
# # # #     print("format verniy :)")
# # # #     print(f"{h}:{m}:{s}")
# # #
# # # ticket = input("vvedi nomer bileta (6 cifr): ")
# # # if len(ticket) == 6 and ticket.isdigit(): # .isdigit число ли это
# # #     # [начало:конец:шаг]
# # #     first_half = ticket[:3]
# # #     last_half = ticket[-3:]
# # #     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
# # #     last_sum = int(last_half[0]) + int(last_half[1]) + int(last_half[2])
# # #     if first_sum == last_sum:
# # #         print("yra pobeda")
# # #     else:
# # #         print("neyra nepobeda")
# # # else:
# # #     print("la ti krisa")
# #
# # month = input("vvedi chislo").strip() # убрать пробелы
# # if month.isdigit() and 12 >= int(month) >= 1:
# #     month = int(month)
# #     if 3 <= month <= 5:
# #         print("vesna")
# #     elif 6 <= month <= 8:
# #         print("leto")
# #     elif 9 <= month <= 11:
# #         print("osen'")
# #     else:
# #         print("Zima")
#
# xomaki = int(input("ckoka xomakov:"))
# if 11 <= xomaki <= 19:
#     print(xomaki, "Хомяков")
# elif xomaki % 10 == 1:
#     print(xomaki, "Хомяк")
# elif 2 <= xomaki % 10 <= 4:
#     print(xomaki, "Хомяка")
# else:
#     print(xomaki, "Хомяков")