from datetime import datetime

weekday_ings = [
    ['Salami', 'Tomatoes', 'Cheese', 'Olives'],
    ['Chicken', 'Pinaple', 'Corn', 'Pepper'],
    ['Bacon', 'Tomatoes', 'Cheese', 'Pepper'],
    ['Mozzarella', 'Gorgonzola', 'Parmigiano Reggiano', 'Goat cheese'],
    ['Shrimps', 'Squids', 'Tomatoes', 'Pepper'],
    ['Beef', 'Mushrooms', 'Tomatoes'],
    ['Salami', 'Mushrooms', 'Pepper', 'Olives']
]

prices = {
    'Salami' : 30, 'Tomatoes' : 15, 'Cheese' : 15, 'Olives' : 20, 'Chicken' : 40, 'Pinaple' : 25, 'Corn' : 15,
    'Pepper' : 25, 'Bacon' : 30, 'Mozzarella' : 20, 'Gorgonzola' : 20, 'Parmigiano Reggiano' : 20, 'Goat cheese' : 15,
    'Shrimps' : 35, 'Squids' : 45, 'Beef' : 35, 'Mushrooms' : 20
}

class Pizza:
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], list):
            self.base = args[0]
        else:
            self.base = []
            for ing in args:
                self.base.append(ing)
        self.additional = kwargs.get('add')
        self.price = self.parsepizza()

    def parsepizza(self):
        price = 0
        for ing in self.base:
            price += prices.get(ing)
        new_add = []
        if self.additional:
            for ing in self.additional:
                try:
                    price += prices.get(ing)
                    new_add.append(ing)
                except TypeError:
                    pass
        self.additional = new_add
        return price

    def getprice(self):
        return self.price

    def __str__(self):
        based = ''
        for ing in self.base:
            based += ing + '\n'
        add = ''
        for ing in self.additional:
            add += ing + '\n'
        if add == '':
            add += 'None\n'
        out = "Your pizza have:\n" + based + "Addidional ingredients:\n" + add
        return out


class PizzaOfTheDay(Pizza):
    def __init__(self, *args):
        todays = weekday_ings[datetime.today().weekday()]
        super().__init__(todays, add=args)


p1 = PizzaOfTheDay()
p2 = PizzaOfTheDay('Mozzarella')
p3 = Pizza('Cheese', 'Mozzarella')

print(p1)
print(p2)
print(p3)
print('Price of 3 pizza is', p3.getprice())