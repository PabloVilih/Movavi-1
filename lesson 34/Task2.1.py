x = ["Никита", "Екатерина", "Арсалан", "Наталья", "Григорий", "Евгений", "Анастасия", "Андрей", "Евгения", "Герман", "Тимур", "Ярослава", "Есения", "Даниил", "Данил"]
person_name = input().capitalize()

kol_vo = 0

for name in x:
    if person_name == name:
        kol_vo += 1
print(person_name)
print(kol_vo)