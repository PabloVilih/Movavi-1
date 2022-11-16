import random as r
import foto_babidjona

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

print(foto_babidjona.intro)
world_answer = r.choice(vocabulary).lower()
world_display = []

for _ in range(len(world_answer)):
    world_display.append("_")

print(world_display)
life = 6
counter = 0 # счётчик проявленных букв

while life > 0 and counter != len(world_answer): # пока есть жизни и не все буквы отгаданы
    print(foto_babidjona.stages[life])
    letter = input("Буква: ")
    letter_is_be = False # наличие букв в слове
    for i in range(len(world_answer)): # пробегаемся по слову
        if letter == world_answer[i]: # если буква равна букве из сова
            if world_display[i] != "_":
                letter_is_be = True
            else:
                world_display[i] = letter # Переворачиваем букву
                letter_is_be = True
                counter += 1

    if letter_is_be == False:
        life -= 1
    print(world_display)
if counter == len(world_answer):
    print("аааа ура")
else:
    print(foto_babidjona.stages[life])
    print("Ну ты и мох")