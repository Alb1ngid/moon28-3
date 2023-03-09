people = (
    "1Батырхан 15 лет",
    "1Абил 14 лет",
    "1Emir 17",
    '1Даниель 16 лет',
    "1улан 19",
    '1жаннат 19',
    '1Жетиген',
    '1бекболот 18'
)

kat = 'Бека'


def may(a):
    print(a, 'мяукает')


# may(kat)


print(type(kat))


# коробка для создания данных
# все функции внутри класса называются -- методами


class Kat:
    hvost = True
    usiki = True

    # конструктор класса
    # магический метод
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def m(self):
        self.may()

    def may(self):
        print(self.name, 'may')

    def __len__(self):
        return len(f'{self.name}')

    def __str__(self):
        return f'my name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'a im a cat\n' \
               f'{self.hvost}\n' \
               f'#########'
kat2 = Kat('Арген', 4, 'оранжевый')
kat2.name = 'Адыл'
kat3 = Kat('emir', 2, 'red')
kat2.m()
print(len(kat2))
print(kat2)
print(kat3)