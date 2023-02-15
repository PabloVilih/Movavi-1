# f = open("восьмой бэ дежурный класс.txt", "w", encoding="utf-8")
# f.write("Ноль\nОдин")
# f.close()

# f = open("восьмой бэ дежурный класс.txt", "r", encoding="utf-8")
# # t = f.read()
# t1 = f.readlines()  # файл разбили по линиям в список
#
# print(t1)
# for line in t1:
#     print(line.rstrip())  # rstrip() - убирает пустоты справа

# 1 задача.

# a = input('введи название файла ')
# f = open(a, 'w', encoding='utf-8')
# b = input('введи че хошь ')
# while b != '':
#     f.write(b + '\n')
#     b = input('введи ')
# print('файл записан')
# f.close()

# a = input('введи название ')
# f = open(a, 'r', encoding='utf-8')
# b = f.readlines() # список строк
# f.close()
# print(b)
# f = open(a, 'w', encoding='utf-8')
# n = 0
# print(b)
# for line in b:
#     n += 1
#     f.write(f'{n}) {line.rstrip()}\n')

# f = open('tadjik artem.txt', "r", encoding='utf-8')
# b = f.readlines()
# print(b)
# n = 0
# while b != []: # пока список не empty
#     d = b[:3] # зафиксировали 3 элемента
#     del b[:3]
#     stas = open(f'{n}.txt', 'w', encoding='utf-8')
#     for i in d:
#         stas.write(i)
#     stas.close()
#     n += 1


a = open("file.txt", "r", encoding="utf-8")
fylesi = a.readlines()
print(fylesi)
chislo = int(input("Почем пиццца: "))
result = fylesi[-chislo:]
print(result)
