class Father:
    def house(self):
        print("Father owns a house")

class Son(Father):
    def car(self):
        print("Son owns a car")


s = Son()
s.house()
s.car()
