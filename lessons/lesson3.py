# 1 Наследование
# object

# 2 плиморфизм

# 3 инкапсуляция
# открытый
# _ = защищенный
# __ = скрытый


class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self.__money = money
        self._key = key

    def __str__(self):
        return f'{self.name}:{self.__money}'

    def keys(self):
        self.__printKey()

    def __printKey(self):
        print(self._key)

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money


user = Bank('Жаннат', 4_000_000, '12edswadw')
user1 = Bank('Жаннат', 4_000_000, '12edswadw')
user2 = Bank('Жаннат', 4_000_000, '12edswadw')
user3 = Bank('Жаннат', 4_000_000, '12edswadw')
user5 = Bank('Жаннат', 4_000_000, '12edswadw')

user.set_money(3000)
print(user.get_money())

# user.keys()
# user._key = '1234'
# user._printKey()
# user.keys()
# print(user._key)


# user._Bank__money = 10000000000

print(user)

print(user.__dir__())
# object._Class__metod()
