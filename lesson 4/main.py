# # # # # # # # fam = input("Фамилия:") .capitalize()
# # # # # # # # name = input("Имя:") .capitalize()
# # # # # # # # otch = input("Отчество:") .capitalize()
# # # # # # # #.capitalize() первая буква заглавная
# # # # # # # # print(fam, name[0] + ".", otch[0] + ".")
# # # # # # # # print(f"{fam} {name[0]}. {otch[0]}.")
# # # # # # # # a = int(input("Число:"))
# # # # # # # # b = int(input("Число:"))
# # # # # # # # c = a + b + 1
# # # # # # # # print(c)
# # # # # # # x = "abracadabra"
# # # # # # # print(x.count("a"))
# # # # # # # # подсчет .count()
# # # # # # x = "Hello World"
# # # # # # lst = x.split(" ")
# # # # # # lst.remove("Hello") # удаление по значению "Hello"
# # # # # # lst.pop(0) # удаление по индексу [0]
# # # # # phrase = input("Введи фразу:")
# # # # # find = input("Что меняем:")
# # # # # replase = input("Введи фразу:")
# # # # #
# # # # # print(phrase.replace(find, replase))
# # # # #
# # # # # abs = {
# # # # #     "а": "a",
# # # # #     "б": "b",
# # # # #     "в": "v",
# # # # #     "г": "g",
# # # # #     "д": "d",
# # # # #     "е": "e",
# # # # #     "ё": "yo",
# # # # #     "ж": "zh",
# # # # #     "з": "z",
# # # # #     "и": "i",
# # # # #     "й": "y",
# # # # #     "к": "k",
# # # # #     "л": "l",
# # # # #     "м": "m",
# # # # #     "н": "n",
# # # # #     "о": "o",
# # # # #     "п": "p",
# # # # #     "р": "r",
# # # # #     "с": "s",
# # # # #     "т": "t",
# # # # #     "у": "y",
# # # # #     "ф": "f",
# # # # #     "х": "x",
# # # # #     "ц": "c",
# # # # #     "ч": "ch",
# # # # #     "ш": "sh",
# # # # #     "щ": "sha",
# # # # #     "ъ": "",
# # # # #     "ы": "ы",
# # # # #     "ь": "",
# # # # #     "э": "a",
# # # # #     "ю": "yu",
# # # # #     "я": "ya",
# # # # #     " ": " ",
# # # # #     ".": ".",
# # # # #     ",": ",",
# # # # #
# # # # # }
# # # # # x = input("Введи фразу:")
# # # # # perevod = ""
# # # # # for bukva in x:
# # # # #     perevod = perevod + abs[bukva]
# # # # # print(perevod)
# # # # x = input("Почта:")
# # # # temp = x.split("@")
# # # # print("Логин:", temp[0])
# # # # print("Домен:", temp[-1])
# # # x = 5
# # # if x == "5":
# # #     print("Ура")
# # while True:
# #     print("2+2=5")
# x = int(input("vvedi chiclo:"))
# if x < 0:
#     print("Otricatelnoe")
# elif x > 0:
#     print("Polozhitelnoe")
# else:
#     print("nol")
year = int(input("Год:"))
# //- целое деление
# %- остаток от деления

if year % 4== 0 and year % 400 == 0 or year % 100 == 0:
    print("God visokosnыy")
else:
    print("God nevisokosnыy")