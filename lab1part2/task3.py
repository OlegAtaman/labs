class Product:
    def __init__(self, price, desription, dimensions):
        self.price = price
        self.destription = desription
        self.dimensions = dimensions

class Customer:
    def __init__(self, name, surname, patronymic, number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.number = number


class Order:
    def __init__(self, customer, products):
        self.cust = customer
        self.products = products

    def cacl(self):
        summary = 0
        for i in range(len(self.products)):
            summary = summary + self.products[i].price
        return summary

terorist = Customer('Sample', 'User', 'Userovich', 'HIS NUMBER')
himars = Product(350000, 'Really good thing', [22, 64, 27])
atacms = Product(15000, 'Ammo for himars', [1, 3, 3])
stinger = Product(3000, 'Cheap but effective', [3, 5, 12])


new_order = Order(terorist, [himars, atacms, stinger])
print(new_order.cacl())