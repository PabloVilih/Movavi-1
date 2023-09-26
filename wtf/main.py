# ООП: инкапсуляция, полиморфизм, наследование

class Human:
    def say(self, phrase): #публичный
        self.__vdoh() #вызов привотного метода только внутри класса
        return "MQ," + phrase

    def __vdoh(self): # приватный
        print("*كلام فارغ*")

    def __init__(self): # маггеический метод
        self.age = 5 # атрибут динамический



petr = Human() # создание объекта на основе класса -> init
print(petr.say("ку"))
print(petr._Human__vdoh()) # фуууууууууууууубллллллл
igor = Human()
print(petr.age)