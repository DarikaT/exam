class CoffeеMachine:
    def __init__(self, milk=1000, coffee=1000, sugar=1000):
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar

    def make_coffee(self, milk=int(input('Кол-во молока: \n')),
        coffee =int(input('Кол-во кофе: \n')),
        sugar=int(input('Кол-во сахара: \n'))):

        if milk <= self.milk and coffee <= self.coffee and sugar <= self.sugar:
            print(self.__subtract({'milk':milk,
                    'coffee':coffee,
                    'sugar':sugar}))

        else:
            print(f"{'Недостаточно ' + str(milk - self.milk) + ' молока. ' if milk - self.milk > 0 else ''}"
                f"{'Недостаточно ' + str(coffee - self.coffee) + ' кофе. ' if coffee - self.coffee > 0 else ''}"
                f"{'Недостаточно ' + str(sugar - self.sugar) + ' сахара. ' if sugar - self.sugar > 0 else ''}")

    def __subtract(self, dict_):
        self.milk -= dict_['milk']
        self.coffee -= dict_['coffee']
        self.sugar -= dict_['sugar']
        return 'Процесс приготовления кофе завершен!'

coffee = CoffeеMachine()
coffee.make_coffee()