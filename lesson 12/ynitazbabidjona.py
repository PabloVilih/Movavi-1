from collections import namedtuple

citizen = namedtuple("Житель", "Имя возраст статус")
alexey = citizen(имя="Лёха Лепёха", возраст=27, статус="Уличный гонщик")

print(alexey)