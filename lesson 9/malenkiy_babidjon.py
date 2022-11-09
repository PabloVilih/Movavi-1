import random as r

logo = """
|\                /|        ______         \        /
|  \            /  |      /        \        \      /
|    \        /    |    /            \       \    /
|      \    /      |  /                \      \  /
|        \/        |  |                |       \/
|                  |  |                |       /\
|                  |  \                /      /  \
|                  |    \            /       /    \
|                  |      \        /        /      \
|                  |        ______         /        \
"""
leng = 3
life = 10

answer = r.randint(100, 999)
answer = str(answer) # число в строку
answer = list(answer) # строчка в список

print(answer)

is_guess = False

while life:  # while life != 0
    is_guess = False
    print("=" * 10)
    print(f"Жизней: {life}")

    guess = input("Число: ")
    if len(guess) != 3 or not guess.isdigit():
        print("Пошел от сюда")
        continue

    if list(guess) == answer:
        print("Победа!")
        is_guess = True
        break # Выход из while

    if not is_guess:
        for i in range(0, leng):
            if guess[i] == answer[i]: #совпадение позиций
                print("SUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
                is_guess = True
                break
    if not is_guess:
        for char in guess:
            if char in answer:
                print("50%")
                is_guess = True
                break
    if not is_guess:
        print("МОХ")

    life = life - 1

print(logo)