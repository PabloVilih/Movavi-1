# # # def flopa(spisok:list) -> int:  # type hinting подсказка
# # #     """Тут надо написать шо це таке"""
# # #     s = 0
# # #     for element in spisok:
# # #         s += element
# # #         return s
# # #
# # #
# # # lst = [5, 6, 4, 1, 3 ]
# # # print(flopa(lst))
# #
# # def join(razdelitel, stroka):
# #     tekst = ""
# #     for element in stroka:
# #         tekst += element + razdelitel
# #     return tekst
# #
# #
# #
# # lst = ["Владимир", "Путин", "взломал", "пентагон"]
# # magamed = "|"
# #
# # print(join(razdelitel=magamed, stroka=lst))
#
# def factorial(chislo:int):
#     eche_chislo = 1
#     for element in range(2, chislo + 1):
#         eche_chislo *= element
#     return eche_chislo
#
#
# print(factorial(chislo=3))

def  okfy98yg(stroka:int):
    ban = {"верх": 0,
           "нижний": 0}
    for i in stroka:
        if i.isupper():
            ban["верх"] += 1
        elif i.islower():
            ban["нижний"] += 1
    return ban


print(okfy98yg())