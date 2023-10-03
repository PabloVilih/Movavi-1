# # # 5 + 2. + оператор 5, 2 операнды
# #
# # # ООП:
# # # 1) инкапсуляция: Приватное и публичное
# # # 2) наследование: Родительский и дочерние классы, super
# # # 3) полиморфизм: Магические методы
# #
# #
# # # инкапсуляция
# # # class Urok:
# # #     shkola = 123432 # статический публичный атрибут
# # #
# # #     __sikeret = 1234 # статический приватный атрибут
# # #
# # #     def __init__(self, dlen): # магический метод
# # #         self.delitelnost = dlen # динамический публичный атрибут
# # #         self.__sikeret2 = 321 # Динамический приватный метод
# # #
# # #     def get5(self):    #публичный метод
# # #         return 5
# # #
# # # matimatika = Urok(50) #инициализация -> создание объекта на основе класса
# # # print(matimatika.get5()) # 5
# # # print(matimatika.delitelnost) # 40
# # #
# # # fizica = Urok(10)
# # # print(fizica.shkola) # вызов статического атрибута
# # # Urok.shkola = "жиж" # меняем статический атрибут
# # # print(matimatika.shkola)
# #
# #
# # # полиморфизм
# # class higa:
# #     def __call__(self, *args, **kwargs):
# #         print(*args, **kwargs)
# #         return "шкебиди доп"
# #
# #     def __add__(self, other): # ПРИ СЛОЖЕНИИ.
# #         return f"{self} + {other}"
# #
# #
# # class giga:
# #     def __str__(self):  # str() и print()
# #         return "ы"
# #
# #
# # hi = higa() # __init__
# # gi = giga() # __init__
# #
# # print(hi()) # __call__
# # print(gi)
# # print(hi + gi)
# # print(hi.__add__(gi)) # строка выше это то же самое
#
#
# # наследование
#
# class c1:
#     def __init__(self):
#         self.shkebede = "доп"
#
#     def say_hi(self):
#         print("hi_hitl")
#
# class c2(c1):  # c2 наследник c1
#     def __init__(self):
#         super().__init__() # вызов init c1 из c2
#         self.skib = "sdfg"
#
# obeje = c1()
# print(obeje.shkebede)
# obejekte = c2()
# print(obejekte.skib)
# print(hasattr(obejekte, "skib")) # есть ли атрибут skib у obejekte
# print(getattr(obejekte, "skib")) # получить skib у obejekte

