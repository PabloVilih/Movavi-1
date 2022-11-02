# # # # # #                              Библиотеки
# # # # # # import random
# # # # # # number = random.randint(0, 100)
# # # # #
# # # # # # import random as r
# # # # # # print(r.randint(0, 100))
# # # # #
# # # # # # from random import randint
# # # # # # print(randint(0, 100))
# # # # #
# # # # # # from random import *  # импортировать все (так лучше не делать)
# # # # # # print(randint(0, 100))
# # # # #
# # # # # import random as r
# # # # #
# # # # # spisok = [1, 2, 3, 4, 5]
# # # # # print(r.choice(spisok)) # choice выбор случайнога числа
# # # # # r.shuffle(spisok)   # shгffle перемешать содержимое
# # # # # print(spisok)
# # # #
# # # # import turtle
# # # #
# # # # screen = turtle.Screen()
# # # # t = turtle.Turtle()
# # # # horizontal = 200
# # # # vertical = 100
# # # # t.color("dark green", "yellow")   # цвет линии, цвет заливки
# # # # t.pensize(5) # толщина линии
# # # # t.speed(3)
# # # # # 1 самая медленная
# # # # # 10 очень быстрая
# # # # # 0 максимальная
# # # #
# # # # t.begin_fill()
# # # # t.forward(horizontal)
# # # # t.right(90)
# # # # t.fd(vertical) #forward
# # # # t.rt(90)  #right
# # # # t.fd(horizontal)
# # # # t.rt(90)
# # # # t.fd(vertical)
# # # # t.rt(90)
# # # # t.end_fill()
# # # #
# # # # t.penup() #поднять перо
# # # # t.goto(120, -30)
# # # # t.fd(50)
# # # # t.pendown()
# # # #
# # # # t.circle(20)
# # # # t.color("blue")
# # # # t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")
# # # #
# # # #
# # # # screen.exitonclick() # выход при клике
# # #
# # # import random as r
# # # import time as t
# # # hacked = 0
# # #
# # # while hacked < 100:
# # #     hacked = hacked + r.randint(1, 10)
# # #     if hacked >= 100:
# # #         print("Прогресс: 100%")
# # #     else:
# # #         print(f"Прогресс: {hacked}%")
# # #     t.sleep(1)
# #
# # import random as r
# # variant = ["1", "2", "3"]
# # guess = input("Где шарик? 1, 2, 3")
# # answer = r.choice(variant)
# # if guess == answer:
# #     print("Четко")
# # else:
# #     print("БААААААААН -----> ", answer)
# import random
# import turtle
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
# colors = ["red", "blue", "yellow", "pink", "green", "black"]
#
# i = int(input("Введи количество углов"))
# side = 100
#
# for j in range(0, i):
#     t.color(random.choice(colors))
#     t.fd(side)
#     t.rt(360/i)
#
# screen.exitonclick()

import random as r
import time as t

print("Жепа тебе сталкер")

is_game = True
while is_game:
    patron = r.choice([1, 2, 3, 4, 5, 6])
    our = r.choice([1, 2, 3, 4, 5, 6])

    print("Заряжаем револьвер")
    t.sleep(2)
    print("Крутим барабан")
    t.sleep(2)
    print("Выстрел через")
    t.sleep(0.5)
    print(3)
    t.sleep(0.5)
    print(2)
    t.sleep(0.5)
    print(1)
    t.sleep(0.3)
    print("ВЫЫЫЫЫЫЫЫЫЫСТРЕЛ")

    if patron == our:
        print("1 прогиб и ты погиб")
        is_game = False
    else:
        print("Прогиб не удался")
        if (input("Готов ли ты получить прогиб?") == "нет"):
            is_game = False

