# print(ord('a'))
# print(chr(5))
#
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# pendos_alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet2 = alphabet[::-1]
# pendos_alphabet2 = pendos_alphabet[::-1]
#
# y = ""
# a = 0
#
# x = input("Что будем шифровать? >>> ").lower()
# if x[0] in pendos_alphabet:
#     a = 0
# else:
#     a = 1
#
# for i in x:
#     if a == 1:
#         if i not in alphabet:
#             y += i
#         else:
#             y += alphabet2 [alphabet.index(i)]
#     else:
#         if i not in pendos_alphabet:
#             y += i
#         else:
#             y += pendos_alphabet2 [pendos_alphabet.index(i)]
# print(y)
#
# a = input()
#
# a = input("uihfuie: ")
# n = int(input("uigfisegfu: "))
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# fraz = ""
# for i in a:

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
fraz = "ЫНУЪЫ, УЧЫЧЩДТ ЮЧЫНФЧЪЕ ЙД АЫЧЙД ЩИРЛИМИФС..."
cs = "ТЕКСТ"
frazer = ""
c = 0

for i in fraz:
    if i in alphabet or i == "":
        frazer +=i
mas = frazer.split(" ")
for shift in range(1,33):
    ghj = ""
    for leter in cs:
        c = alphabet.index(leter)
        c = (c + shift)%33
        ghj += alphabet[c]
    if ghj in mas:
        print("Сдвиг равен", shift)
        break
