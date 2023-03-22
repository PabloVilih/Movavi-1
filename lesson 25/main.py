# class Oeufgvsh:
#     prosto_kakoeto_znachenie = True  # статический публичный атрибут
#     __prosto_kakoeto_znachenie = True  # статический приватный атрибут
#
#     def __init__(self, x = "Кефтеме"):  # значение по умолчанию
#         self.prosto_kakoeto_znachenie2 = x     # динамический публичный атрибут
#         self.__prosto_kakoeto_znachenie2 = x     # динамический приватный атрибут
#
# obj = Oeufgvsh()
# print(obj.prosto_kakoeto_znachenie2)



class Human:
    default_name = "Loshara13_2018_200Volt_500;)"
    default_age = 1007

    def __init__(self, name = "oleg", age = 34):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        return self.name, self.age, self.__money, self.__house

    def earn_money(self):
        self.__money += 50000

    def default_info(self):
        return self.default_name, self.default_age

    def __make_deal(self, hata):
        """Совершаем ли сделку(по деньгам). Return True || False"""
        if hata.final_price() < self.__money:
            return True
        else:
            return False

    def buy_house(self, hata):
        if self.__make_deal(hata):
            self.__money -= hata.final_price()
            hata.owner = self.name
        else:
            print(f"У тебя есть {self.__money} робуксов, а нужно {hata.final_price()}.\n"
                  f"Иди фарми лес")




class House:
    def __init__(self, __area = 1478, __price = 19374553):
        self.__area = __area
        self.__price = __price

    def final_price(self, skidka):
        return self.__price - self.__price * skidka


chel = Human()
hata = House()
chel.buy_house(hata)