from itertools import count

created_tickets = []
class Ticket:
    cntr = count(1)
    price = 100
    def __init__(self, number=None):
        if number and number not in created_tickets:
            self.id = number
        else:
            self.id = next(self.cntr)
            while self.id in created_tickets:
                self.id = next(self.cntr)
        created_tickets.append(self.id)

    def getprice(self):
        return self.price

    def __str__(self):
        return f'''id - {self.id}  price - {self.price}
Thank you for purchase! Enjoy the event!
_________________________________________'''


class RegularTicket(Ticket):
    def __str__(self):
        out =  """_________________________________________\nRegular ticket\n"""
        out += super().__str__()
        return out


class AdvanceTicket(Ticket):
    def __init__(self, number=None):
        super().__init__(number)
        self.price = int(self.price * 0.6)

    def __str__(self):
        out = """_________________________________________\nAdvance ticket\n"""
        out += super().__str__()
        return out


class StudentTicket(Ticket):
    def __init__(self, number=None):
        super().__init__(number)
        self.price = int(self.price * 0.5)

    def __str__(self):
        out = """_________________________________________\nStudent ticket\n"""
        out += super().__str__()
        return out


class LateTicket(Ticket):
    def __init__(self, number=None):
        super().__init__(number)
        self.price = int(self.price * 1.1)

    def __str__(self):
        out = """_________________________________________\nLate ticket\n"""
        out += super().__str__()
        return out


t1 = RegularTicket()
t2 = StudentTicket(4)
t3 = LateTicket()
t4 = LateTicket()
t5 = AdvanceTicket()

print(t1)
print(t2)
print(t5)
print()
print("Price of 3 ticket is", t3.getprice())
