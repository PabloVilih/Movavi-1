import random as r
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hp = [r.choice(cards)]      #hand player
hc = [r.choice(cards)]      #hand computer
sp = 0                      #score player
sc = 0                      #score computer
getc = "y"                  #get cards
while getc == "y":
    hp.append(r.choice(cards))

    if sum(hp) > 21 and 11 in hp: # если сумма карт > 21 и туз в руке
        for i in range(0, len(hp)):
            if hp[i] == 11:
                hp[i] = 1
                break
    sp = sum(hp)
    print(f"Твоя рука: {hp}. Очков: {sp}")
    print(f"Первая карта диллера: {hc[0]}.")
    if sp > 21:
        getc = "n"   #если перебор то не берём карту
    else:
        getc = input("Добираем карту?")
while sum(hc) < 17:
    hc.append(r.choice(cards))

    if sum(hc) > 21 and 11 in hc: # если сумма карт > 21 и туз в руке
        for i in range(0, len(hc)):
            if hc[i] == 11:
                hc[i] = 1
                break

sc = sum(hc)

print("=" * 10)
print(f"Итоговая рука диллера: {hc}. Очков: {sc}")
print(f"Твоя рука: {hp}. Очков: {sp}")

if sp > 21 and sc > 21:
    if sp > sc:
        print("Победа")
    else:
        print("мох")
elif sp > 21:
    print("мох")
elif sc > 21:
    print("Ну молодец")
elif sp == sc:
    print("Ничья")
elif sp > sc:
    print("Победа")
else:
    print("мох")