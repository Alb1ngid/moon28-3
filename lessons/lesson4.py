# множественное наследование
class A:
    def __init__(self, a):
        self.a = a

    def set(self):
        print('это метод класса А')


class B(A):
    pass


class C:
    def set(self):
        print('это метод класса С')

    def __init__(self, c):
        self.c = c


class M(C, B):
    def __init__(self, a, c):
        B.__init__(self, a)
        C.__init__(self, c)

    def __str__(self):
        return f"{self.a} {self.c}"

    def set(self):
        C.set(self)
        super().set()
        A.set(self)
m = M('A', 'C')
print(m)
print(M.mro())
m.set()
# C.set(m)
