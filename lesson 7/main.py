# # # # # x = 7/0 #ZeroDivisionError:
# # # # # x = 7 + "hhh" #TypeError:
# # # # # x = [0, 4, "sdfsdfsdf"]
# # # # # print(x[3]) #IndexError:
# # # # # x = "я дурачёк который забывает ставить вторые ковычки
# # # # #SyntaxError:
# # # # #int("A")  #ValueError:
# # # # # print(x) #NameError:
# # # # # assert
# # # # def summa(numbers):
# # # #     return sum(numbers)
# # # #
# # # # assert summa([1, 2]) == 3
# # # # assert summa([1, 2]) == 4 #AssertionError
# # # try:
# # #     div = int(input("введи число для деления: "))
# # #     x = 5/div
# # # except ZeroDivisionError: #обработка деления на ноль
# # #     print("ЭЙ ТЫ! Ты ошибка деления на ноль")
# # # # except Exception: #Обработка любой ошибки
# # # #     print("Ошииииииииииииииииииииибка")
# # # except ValueError:
# # #     print("Цифру!!!!!!!!!!"")
# # # else:
# # #     print("Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо Все шорошо         аркпраыклупаркыупимувамилыораугпкывармтвапмикоуавпамирув")
# #
# # lst = []
# # try:
# #
# #     f = open("file1.txt")  # файл помещён в f
# # except ModuleNotFoundError:
# #     print("нету фуйла, иди от сюда")
# # try:
# #     for line in f:  #для каждой строчки в файле
# #         lst.append(int(line))   # добавить в список число
# # except ValueError:
# #     print("Я хочу только цифры ыыыыыыыыыыыыыы")
# # else:
# #     print("НОООООООООООРМ")
# # finally:
# #     f.close()
# # print(lst)
# # try:
# #     x = 5/0
# # except ZeroDivisionError as error_message:
# #     print("тут ошибка", error_message)
#
# x = input("введи любое имя: ").lower().strip()
# try:
#     if x == "антон":
#         raise Exception("Имя моего преподователя запрещено")
# except Exception:
#     print("мовави топ за антона стеной")

# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     pass # затычка нечего
#
# if 5 == 2:
#     pass



import random
while True:
    print("Угадай число")
    mini = 0
    maxi = 0
    computer_number = random.randint(0, 100)
    life = 7
    while life > 0:
        user_number = int(input("Введи число: "))
        if user_number < 0 or user_number > 100:
            print("Введи число от 0 до 100")
            continue
        if computer_number == user_number:
            print("Вы победили!")
            break
        elif computer_number < user_number:
            print("Нужно меньше.")
            maximum = user_number
        else:
            print("Нужно больше.")
            minimum = user_number
        print(f">>> Интервал: {mini} – {maxi}")
        life = life - 1
        print("❤️:", life)
    answer = input("Хочешь продолжить?")
    if answer == "Да":
        continue
    else:
        break