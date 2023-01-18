from pictyres import box_carrot, box_empty, box_close
from random import choice


def generate_boxes(status1, status2):
    result = ""
    if status1 == "ПУСТОТА":
        box1 = box_empty.format(COLOR1.center(13)).split("\n")
    elif status1 == "МОРКОВКА":
        box1 = box_carrot.format(COLOR1.center(13)).split("\n")
    else:
        box1 = box_close.format(COLOR1.center(13)).split("\n")

    if status2 == "ПУСТОТА":
        box2 = box_empty.format(COLOR2.center(13)).split("\n")
    elif status2 == "МОРКОВКА":
        box2 = box_carrot.format(COLOR2.center(13)).split("\n")
    else:
        box2 = box_close.format(COLOR2.center(13)).split("\n")

    for element in zip(box1, box2):
        result += "   ".join(element) + "\n"
    result += p1Name[:10].center(13) + " " * 7 + p2Name[:10].center(13) + "\n"
    return result


COLORS = ["ФИОЛЕТОВАЯ", "КАЙФОВАЯ", "МАГАДНСКАЯ", "УНЫЛАЯ"]
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)
while COLOR1 == COLOR2:  # чтобы было(цвета разные)
    COLOR2 = choice(COLORS)

p1Box = "ЗАКРЫТО"
p2Box = "ЗАКРЫТО"

p1Name = input(">>> Имя первого игрока: ")
while p1Name.strip() == "":  # Если убрав пробелы останется пустота
    p1Name = input(">>> Имя первого игрока: ")

p2Name = input(">>> Имя второго игрока: ")
while p2Name.strip() == "":
    p2Name = input(">>> Имя второго игрока: ")

print(generate_boxes("ПУСТОТА", "мОХ"))

while True:
    print(f"{p2Name}, в твоей коробке {p2Box}")

    # БЛЕФ / ПРАВДА
    action = input(f"Нужно сделать выбор:\n"
                   f"1. Блеф: сказать что в коробке {p1Box}\n"
                   f"2. Правда: суазать что в коробке {p2Box}\n"
                   f">>> (Б - Блеф, П - Правда) -> ").upper()

    while action != "Б" and action != "П":
        action = input(f">>> (Б - Блеф, П - Правда) -> ").upper()

    print("\n" * 100)
    input(f">>> {p1Name} открывает глаза(Enter)...")
    if action == "Б":
        print(f"{p2Name} сообщает, что в его коробке {p1Box}")
    else:
        print(f"{p2Name} сообщает что в его коробке {p2Box}")

    #Обмен
    change = input("Тебе нужно решить, меняетесь ли вы коробками\n"
                   "Д(меняться) или Н(не меняться) >>>").upper()
    if change == "Д":
        p1Box, p2Box = p2Box, p1Box  #Меняем содержимое коробок
        input(f"{p1Name} закрывает глаза,  (Enter...)")

        if p2Box == "МОРКОВКА":
            box2 = box_carrot.format(COLOR2.center(13)).split("\n")
        else:
            box2 =  box_empty.format(COLOR2.center(13)).split("\n")
    else:
        break
print("========================= Результаты: ============================")
print(generate_boxes(p1Box, p2Box))
if p1Box == "МОРКОВКА":
    print(p1Name, "Победил")
else:
    print(p2Name, "Победил")