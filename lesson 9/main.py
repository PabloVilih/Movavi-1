# # # # #for
# # # # lst = ["А", "Б", "В", "Г", "Д"]
# # # # for element in lst:
# # # #     print(element)
# # # #
# # # # for index in range(0, 5):
# # # #     print(index)
# # #
# # # #while
# # # x = 10
# # # while x !=0:
# # #     print(x)
# # #     x -= 1
# #
# # word = input("Введи слово: ")
# # while word: # работает пока ворд не пустой (из-за того что это строка)
# #     print(word, end=" ")
# #     word = word[:-1]
#
# number = int(input("Введи число: "))
# while number: # пока
#
#
#
#
#

step = 0
x = int(input("Введи число: "))
while x != 1:
    step += 1

    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "/")
        x = x // 2 # // для того чтобы было не 13.0 а 13
    else:
        x = x * 3 + 1
    print(x)
print("Всего шагов:", step)