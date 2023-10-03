# # # # # def add_one(a, b):
# # # # #     return a + b + 1
# # # # #
# # # # # add_one2 = lambda a,b: a + b + 1  # Анологичная лямбда функция
# # # # #
# # # # # result = lambda answer: True if answer == "Д" else False # if-else Внутри lambda
# # # # #
# # # #
# # # #
# # # #
# # # #
# # # # # List comprehension
# # # #
# # # # # List comprehension
# # # # 1 import random as r
# # # #
# # # # lst = []
# # # #
# # # # for i in range(5):
# # # #     lst.append(r.randint(1,5))
# # # # print(lst)
# # # #
# # # # lst2 = [r.randint(1, 5) for n in range(1, 6)]
# # # # #1. List comprehension Всегда пишется в []
# # # # #2. for n in range() - Обычный цикл for -> сколько элементов будет в списке
# # # # #3. Перед for -> сам добавляемый элемент
# # # # print(lst2)
# # # #
# # #
# # #
# # # # Задача 1
# # #
# # # c2f = lambda c: 9/5 * c + 32
# # # print(c2f(200))
# # #
# # # f2c = lambda f: (f - 32) * 5/9
# # # print(f2c(200))
# # #
# # # c2k = lambda c: c + 273.15
# # # print(c2k(200))
# # #
# # # k2c = lambda k: k - 273.15
# # # print(k2c(200))
# # #
# # # f2k = lambda f: c2k(f2c(f))
# # # print(f2k(200))
# #
# #
# 1 import random as r
#
# while True:
#     lst = []
#     kol_vo_kybikov = int(input("Сколько кубиков бросаем?: "))
#     lst = [r.randint(1, 6) for i in range(kol_vo_kybikov)]
#     print(lst)
#     if_break = input("Выходим? (Д/Н) ").upper()
#
#     if if_break == "Д":
#         break
#
#
# # from random 1 import choice
# #
# # chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
# #          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
# #          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
# #          list("abcdefghijklmnopqrstuvwxyz"),
# #          list("1234567890")
# #         ]
# # a = "https://www.google.com"
# # dict = {}
# # f = [choice(choice(chars)) for i in range(6)]
# # b = "".join(f)
# # print(b)
# # if a in dict:
# #     print("ладно", dict[a])
# # else:
# #     dict[a] = b
# # print("cskrf lj,fdktyf", dict[a])


# Задача 5

field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]

def krytoy_cucumber() -> None:
    '''отрисовывает '''
    print(" 1 2 3 ")
    for row in range(3):
        print(cell_letter[row], end="")
        for column in range(3):
            print(list(field.values())[row][column], end="")
        print("\n")


def krytoy_potatoe()

krytoy_cucumber()