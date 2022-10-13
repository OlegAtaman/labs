class Product:
    def __init__(self, name='product', price=0, desription='', dimensions=[1,1,1]):
        if price < 0:
            price = 0

        self.desription = desription
        self.dimensions = dimensions
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Customer:
    def __init__(self, name='Customer', surname='', patronymic='', number='XXXXXX'):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.number = number


class Order:
    def __init__(self, customer, products):
        self.cust = customer
        self.products = products
        self.number = len(products)

    def add(self, product):
        if type(product) == Product:
            self.products.append(product)
            self.number += 1
        else:
            raise TypeError("You can add only products")

    def delete(self, product):
        if product in self.products:
            self.products.remove(product)
            self.number -= 1
        else:
            raise Exception("There is not such product")

    def cacl(self):
        summary = 0
        for i in range(len(self.products)):
            summary = summary + self.products[i].price
        return summary


avg_kpi_student = Customer('Sample', 'User', 'Userovich', 'HIS NUMBER')
himars = Product('HIMARS', 350000, 'Really good thing', [22, 64, 27])
atacms = Product('ATACMS', 50000, 'Ammo for himars', [1, 3, 3])
stinger = Product('Stinger', 3000, 'Cheap but effective', [3, 5, 12])
rpg7 = Product('RPG-7', 1000, 'Cheap and less effective', [3, 6, 10])
fv103 = Product('FV-103 Spartan', 100000, 'Better than BMP', [10, 22, 5])

new_order = Order(avg_kpi_student, [himars, atacms, stinger])
new_order.add(fv103)
new_order.delete(himars)
print(new_order.cacl())
