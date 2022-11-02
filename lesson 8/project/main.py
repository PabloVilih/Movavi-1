import additional
import random

print(additional.logo)

score = 0
data = additional.data
a = random.choice(data)
b = random.choice(data)
is_game = True
while is_game:
    print("Твой счет:", score)
    print("-" * 10)
    print(f"A: {a['name']}. {a['description']} из {a['country']}")
    print(additional.vs)
    print(f"B: {b['name']}. {b['description']} из {b['country']}")
    select = input("У кого больше подписчиков? (A, B)").upper().strip()
    if select ==