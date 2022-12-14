# # # # # # # # # множество
# # # # # # # # set() # преобразование ко множеству
# # # # # # # # mySet = {"А", "Б", "В"}  # неупорядоченый тип данных
# # # # # # # # print(mySet)
# # # # # # #
# # # # # # # set_1 = {1, 2, 3, 4, 5}
# # # # # # # set_2 = {3, 4, 5, 6, 7}
# # # # # # # print(set_1 | set_2) # объединение .union()
# # # # # # # print(set_1 & set_2) # пересечение .intersection()
# # # # # # # print(set_1 - set_2) # разность .difference()
# # # # # # # print(set_1 ^ set_2) # симетрическая разность .symmetric_difference()
# # # # # #
# # # # # # # словарь
# # # # # # mydict = {"Ключик1": 1,
# # # # # #           "Ключик2": "Значение2"}
# # # # #
# # # # # from random import randint
# # # # # lst = []
# # # # #
# # # # # for _ in range(5):
# # # # #     lst.append(randint(1, 5))
# # # # # print(lst)
# # # # # xz = set(lst)
# # # # # kolvo = len(xz)
# # # # #
# # # # # lst1 = list(xz)
# # # # #
# # # # # print(f"{kolvo},шт {lst1} ")
# # # #
# # # # from random import randint
# # # #
# # # # lst2 = []
# # # # lst1 = []
# # # #
# # # # size = randint(100, 1000)
# # # #
# # # # r_start = 0
# # # # r_end = 10000
# # # #
# # # # for _ in range(size):
# # # #     lst1.append(randint(r_start, r_end))
# # # #     lst2.append(randint(r_start, r_end))
# # # #
# # # # set1 = set(lst1)
# # # # set2 = set(lst2)
# # # #
# # # # sssr = set1 & set2
# # # #
# # # # print(f"Общих чисел: {len(sssr)}")
# # # # print(f"[Кол-во генераций]: {size}")
# # # # print(f"Минимальное число: {min(sssr)}")
# # # # print(f"Максимальное число: {max(sssr)}")
# # # #
# # # # BAN = list(sssr)
# # # # print(sorted(BAN))
# # #
# # #
# # #
# # # mn_sovsem = set()
# # # insert = ""
# # # mn = set() # пустое множество
# # # while insert != "end":
# # #     insert = input("Введи число: ")
# # #     if insert.lstrip("-").isdigit():
# # #         if insert not in mn:
# # #             print("❌ нет")
# # #             mn.add(insert)
# # #         else:
# # #             print("✔ да")
# # #     elif insert == "end":
# # #         break
# # #     else:
# # #         print("👿 Число хочо")
# #
# # lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# # print(f"{lst1} - возможно есть повторения")
# # set1 = set(lst1)
# # print(f"{set1} - повторений нет")
#
# qwerty = "Я люблю movavi, программирование, а ещё я люблю пельмени!"
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/', ':', ';']
# text = ""
# for char in qwerty.lower():
#     if char not in symbols:
#         text += char
# text = text.split(" ")
# print(text)
# s = set(text)
# print(s)
# print(f"Различных слов: {len(s)}шт")

n = int(input("Количество связей деревьев: "))
gen = {}
for _ in range(n):
    child, parent = input("Ребёнок Родитель: ").split()
    if parent not in gen: # если родителя нет в древе
        gen[parent] = [child]
    else:
        gen[parent].append(child)
print(gen)