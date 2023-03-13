# 1 Наследование
# object
#
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


user = Bank('Жаннат', 4_000_000, '12edswadw')

# user.keys()
# user._key = '1234'
# user._printKey()
# user.keys()
# print(user._key)


user._Bank__money = 10000000000

print(user)

print(user.__dir__())
