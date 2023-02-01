

# easygui.msgbox(
#     msg="Hello World",
#     image="img/Lyti_shrek.png",
#     title="Синий хаги ваги",
#     ok_button="Cцп со........"
# )

# easygui.buttonbox(
#     msg="Куда сядешь?",
#     choices= ("Cтул", "Унитаз"),
#     title=("Интересная задачка")
# )

# number = easygui.integerbox(
#     msg="За сколько купишь ук.....",
#     lowerbound=5,
#     upperbound=123456789,
#     image="img/BOMBA.png"
# )
# print(number)

















import easygui
import random


def rock_peper_stone():
    sosasik ={"cuмень": "img/cum.png",
              "ножницы": "img/noz.png",
              "глад валакас": "img/bym.pmg"}
    result = easygui.buttonbox(
        msg="Я помню пенис большой",
        title="Олег",
        images=["img/cum.png", "img/noz.png", "img/bym.pmg"],
        choices=("Выйти",)
    )
    komp = random.choice(list(sosasik.keys()))
    print(result, komp)
    if result == sosasik["cuмень"] and komp == "cuмень":
        easygui.msgbox(msg="Ничья")
    elif result == sosasik["cuмень"] and komp == "ножницы":
        easygui.msgbox(msg="Ура подеда")
    elif result == sosasik["cuмень"] and komp == "глад валакас":
        easygui.msgbox(msg="Ты промазал хуком")
    elif result == sosasik["ножницы"] and komp == "cuмень":
        easygui.msgbox(msg="Ты про***л мид")
    elif result == sosasik["ножницы"] and komp == "ножницы":
        easygui.msgbox(msg="Ничья")
    elif result == sosasik["ножницы"] and komp == "глад валакас":
        easygui.msgbox(msg="Лайн не про**н")
    elif result == sosasik["глад валакас"] and komp == "cuмень":
        easygui.msgbox(msg="PADGE WIN")
    elif result == sosasik["глад валакас"] and komp == "ножницы":
        easygui.msgbox(msg="Loose gg")
    elif result == sosasik["глад валакас"] and komp == "глад валакас":\
        easygui.msgbox(msg="Ничья")


def guess_the_number():
    life = 7
    number = easygui.integerbox(
        msg="Попробуй угадать число",
        lowerbound=1,
        upperbound=100,
    )
    computer = random.randint(1, 100)
    print(computer)
    while life > 0:
        if number < computer:
            number = easygui.integerbox(
                msg=f"Больше \n"
                    f"Жизней осталось: {life}",
                image="img/bolshe.png",

            )
        elif number > computer:
            number = easygui.integerbox(
                msg=f"Меньше \n"
                    f"Жизней осталось: {life}",
                image="img/menshe.png",
            )
        else:
            easygui.msgbox(msg="ура пабеда")
            break
        life -= 1




games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_peper_stone,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()
