# # # # # # # # # # # # # lst = [5, 7, "7", True]
# # # # # # # # # # # # # lst.append("Мшк Фреде") # .append() добавить мишку фреде в список (натуралов)
# # # # # # # # # # # # # # lst.pop() # .pop() удалить мишку фреде по индексу
# # # # # # # # # # # # # # lst.remove() # .remove() удалить мишку фреде из списка натуралов по имени
# # # # # # # # # # # # #
# # # # # # # # # # # # # lst1 = [0, 1, 2]
# # # # # # # # # # # # # lst2 = ["А", "Б", "В"]
# # # # # # # # # # # # # # [0, 1, 2, "A", "Б", "B"]
# # # # # # # # # # # # # lst1.extend(lst2)
# # # # # # # # # # # # # print(lst1)
# # # # # # # # # # # #
# # # # # # # # # # # # lst = [1, 2, 3]#     0   1   2  3
# # # # # # # # # # # # lst.insert(1, 1.5)# [1, 1.5, 2, 3]
# # # # # # # # # # # # print(lst)
# # # # # # # # # # #
# # # # # # # # # # lst = [1, -3, 7, -9, 2]
# # # # # # # # # # lst.sort(reverse=True) # .sort() - coртировка reverse=True реверс
# # # # # # # # # # print(lst)
# # # # # # # # # #
# # # # # # # # # # lst.clear() # очистить список
# # # # # # # # # # print(lst)
# # # # # # # # #
# # # # # # # # # lst = [5, 4, 3, 2, 1, 0]
# # # # # # # # # lst.reverse() # жестко реверсировать список без регистрации и смс
# # # # # # # # # print(lst)
# # # # # # # #
# # # # # # # # # КОРТЕЖИИИИИИИИИИ - неизменяемый
# # # # # # # # # типы данных = мутабельные(изменяемые) немутабельные(ну вы поняли)
# # # # # # # #
# # # # # # # # x = "mavavi"
# # # # # # # # x[1] = "o" # так низя ТЫ ПОНЯЛ :(
# # # # # # #
# # # # # # # tup = (1, 2, 3)
# # # # # # # tup1 = 1, 2, 3
# # # # # # # tup2 = 1,
# # # # # # #
# # # # # # # print(max(tup))
# # # # # #
# # # # # # a = int(input("Число: "))
# # # # # # b = int(input("Число: "))
# # # # # # lst = []
# # # # # # for jojo_bizzare_adventure in range(a + 1, b):
# # # # # #     lst.append(jojo_bizzare_adventure ** 2)
# # # # # # print(lst)
# # # # #
# # # # # phrase = input(">>>")
# # # # # lst = phrase.split(" ")
# # # # # lst.reverse()
# # # # # print(lst)
# # # #
# # # # chet = 0
# # # # nechet = 0
# # # # lst = []
# # # # number = ""
# # # #
# # # # while number != "end":
# # # #     number = input("Число: ")
# # # #     if number.lstrip("-").isdigit():
# # # #         number = int(number)
# # # #         lst.append(number)
# # # #     elif number == "end":
# # # #         break
# # # #     else:
# # # #         print("Ты Е**** ТЫ ЗАБАНЕН Б**** Я БОЛЬШЕ НЕ БУДУ ТЕБЯ РАЗБАНИВАТЬ ПОТОМУ ЧТО ТЫ ТУПОЙ С***")
# # # #         number = "end"
# # # #     if number % 2 == 0:
# # # #         chet += 1
# # # #     else:
# # # #         nechet += 1
# # # #
# # # # print(f"Чётных: {chet}шт.")
# # # # print(f"Нечётных: {nechet}шт.")
# # #
# # # phrase = input(">>> ")
# # # lst = phrase.split(" ")
# # # print(lst)
# # # for i in range(1, len(lst)):
# # #     if int(lst[i]) > int(lst[i-1]):
# # #         print(f"Я считаю, ")
# #
# # lst = [-5, 14, 2, -8, 1]
# # mini = min(lst)
#
# import random as r
#
# lst = []
# count = int(input("Сколько учеников в строю?"))
# for _ in range(count):
#     lst.append(r.randint(150, 200))
# lst.sort(reverse=True)
# print("Было:", lst)
#
# peter = int(input("Рост Пети: "))
# lst.append(peter)
# lst.sort(reverse=True)
# print("Стало", lst)
#
# revers = lst[::-1]
# peter_position = len(lst) - revers.index(peter)
# print(f"Петя встает {peter_position} по счёту.")

nums = [4, 5, 6, 7, 8, 9, 10]
shift = int(input("Сдвиг: "))
if shift < 0:
    shift = abs(shift)
    for i in range(shift):
        nums.append(nums.pop(0))
else:
    for i in range(shift):
        nums.insert(0, nums.pop())
        #.pop() без индекса это изятие последнего элемента