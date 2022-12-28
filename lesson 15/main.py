# # # # # # # # Множества > подмножества и надмножества
# # # # # # #
# # # # # # # s = {1, 2, 3}
# # # # # # # nad = {0, 1, 2, 3}
# # # # # # # pod = {1, 3}
# # # # # # # miss = {4, 5}
# # # # # # #
# # # # # # # if pod < s:
# # # # # # #     print("Это подмножество S")
# # # # # #
# # # # # # person1 = {"Python", "C#", "Java"}
# # # # # # person2 = {"Python", "YoptaSkript", "Kotlin", "BrainFuck", "C++",}
# # # # # #
# # # # # # if person1 < person2:
# # # # # #     print("Второй крутой. Он знает стек первого.")
# # # # # # elif person2 < person1:
# # # # # #     print("Первый крутой. Он знает стек второго.")
# # # # # # else:
# # # # # #     print("Стеки разработки отличаются.")
# # # # #
# # # # # def Dagistan():  # Обозначили
# # # # #     print("Я умнее чем компьютер у меня памяти 10 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 9 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 8 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 7 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 6 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 5 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 4 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 3 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 2 мегабайт")
# # # # #     print("Я умнее чем компьютер у меня памяти 1 мегабайт")
# # # # #
# # # # # Dagistan() # Вызов функции
# # # #
# # # # def koren(number, stepen):  # Функция с двумя аргументами
# # # #     return number ** (1/stepen) # return возвращение результата
# # # #
# # # #
# # # # c = koren(27, 3)
# # #
# # # l = []
# # # l = input()
# # # def suuuuuuuuuuuuuu(mesi):
# # #     l1 = sorted(l)
# # #     if l1 == l:
# # #         return True
# # #
# # # if suuuuuuuuuuuuuu(l) == True:
# # #     print(1)
# # # else:
# # #     print(0)
# #
# # def aoaoaoaoao(words):
# #     l = []
# #     for alalala in words:
# #         l.append(len(alalala))
# #     maxi = max(l)
# #     badan = l.index(maxi)
# #     return words[badan]
# #
# #
# # spisok = ["да", "ыыыыы", "янекреативный"]
# # print(aoaoaoaoao(words=spisok))
#
# def mmm(spsk):
#     mini, maxi = spsk[0], spsk[0]
#     for i in spsk:
#         if i > maxi:
#             maxi = i
#         if i < mini:
#             mini = i
#     return {"Максимум": maxi, "Минимум": mini}
#
# l = [18, 44, 65, 1, 77]
# print(mmm(spsk=l))
# Множества > подмножества и надмножества
#
# # s = {1, 2, 3}
# # nad = {0, 1, 2, 3}
# # pod = {1, 3}
# # miss = {4, 5}
# #
# # if miss < s:
# #     print("Это подмножество S")
#
# # person1 = {"Python", "C#", "Java"}
# # person1 = {"Python", "C++", "Kotlin"}
# # person2 = {"YoptaScript", "Kotlin", "BrainFuck", "C++", "Python"}
# #
# # if person1 < person2:
# #     print("Второй крутой. Он знает стек первого.")
# # elif person2 < person1:
# #     print("Первый крутой. Он знает стек второго.")
# # else:
# #     print("Стеки разработки отлчичаются.")
#
#
# # ФУНКЦИИ
#
# # def nazvanie_function():  # обозначили
# #     print("5")
# #     print("4")
# #     print("3")
# #     print("2")
# #     print("1")
# #
# # nazvanie_function()  # вызов функции
# # nazvanie_function()  # вызов функции
#
# # def koren(number, stepen):  # функция с двумя аргументами
# #     return number ** (1/stepen)  # возвращение результата
# #
# #
# # print(koren(27, 3))
#
#
# # Первый задача.
# # def roflan(spisok):
# #     s = sorted(l)
# #     if s == spisok:
# #         return True
# #
# # l = [1, 6, 5]
# # # roflan(spisok=l)
# # if roflan(l):
# #     print("отсортированно")
# # else:
# #     print("ливай")
#
#
# # задача 2
#
# # def find_longest(words):
# #     chisla = []
# #     for iek in words:
# #         chisla.append(len(iek)) # добавляем в список длинну каждого слова
# #     maxi = max(chisla) # максимальная длинна из списка
# #     bogdan = chisla.index(maxi) # индекс наибольшей длинны
# #     return words[bogdan]
# #
# #
# #
# # spisok = ["да", "три", "двенцадцать", "arthas"]
# # print(find_longest(words=spisok))
#
#
# # задача 3
# #
# # def min_max(spisok):
# #     mini, maxi = spisok[0], spisok[0]
# #     for i in spisok:
# #         if i > maxi: # нахождение нового максимума
# #             maxi = i # запись нового максимума
# #         if i < mini: # нахождение нового минимума
# #             mini = i # запись нового минимума
# #     return {'максимум': maxi, 'минимум': mini}
# #
# # l = [18, 44, 34, 52]
# # print(min_max(spisok=l))
#
#
# # ЗАДАЧА ЧЕТВЕРТЫЙ.
# # def list_sum(l1, l2):
# #     if len(l1) != len(l2):  # если разные длины
# #         if len(l1) > len(l2):  # если 1-й список больше
# #             for index in range(len(l2)):  # проходимся по второму списку.
# #                 l1[index] += l2[index]  # складываем элементы
# #             return l1  # ответ в первом списке
# #         else:  # если 2-й список длинее
# #             if len(l2) > len(l1):  # если 2-й список больше
# #                 for index in range(len(l1)):  # проходимся по первому списку.
# #                     l2[index] += l1[index]  # складываем элементы
# #                 return l2  # ответ во втором списке
# #
# # lst1 = [10, 20, 30, 40, 50]
# # lst2 = [5, 6, 7]
# #
# # print(list_sum(lst1, lst2))
#
# # ЗАДАЧА ПЯТЫЙ.
#
# def tajik(number):
#     for i in range(2, (number + 1)):
#         if i == number:
#             return True
#         if number % i == 0:
#             break
# print(tajik(4))