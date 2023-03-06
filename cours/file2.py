class CoffeM:
    def __init__ (self, name):
        self.name=name
        self.water_temp=200

    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")

Lavazza=CoffeM("Lavazza")
# print(Lavazza.name)

class CappuccinoM( CoffeM ):
    def __init__(self,name,milk):
        super().__init__(name)
        self.milk = milk
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def affichage(self):
        print(self.name)
        print(self.milk)
        print(self.water_temp)
    def brew_now(self, beans):
        super().brew_now(beans)
        print('greaaaaaaaaaaat')

# express=CappuccinoM("express","complet")
# express.brew_now("brazilian")
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeM("Cafe")
    def make_coffee(self, beans):
        self.cafe.brew_now(beans)


S= Barista("Simple")
print(S.cafe.water_temp)
