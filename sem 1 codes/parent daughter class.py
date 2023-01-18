class A:
    def __init__(self,c):
        self.c=c
    def char(self):
        print(self.c.lower())
class B(A):
    def __init__(self, c):
        self.c=c
    def char(self):
        print(ord(self.c))
    def char1(self):
        print(self.c)
character=input()
a=A(character)
b=B(character)
a.char()
b.char()
b.char1()