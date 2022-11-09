from datetime import date, datetime, timedelta
from uuid import uuid4
import json

data = json.load(open('tickets.json'))
created_tickets = []
for ticket in data.get('tickets'):
    created_tickets.append(ticket.get('id'))

class Ticket:
    id = uuid4()
    def __init__(self, event, number=None):
        self.price = event.price
        self.event = event
        if len(self.event.tickets) == self.event.places:
            raise(ValueError('All tickets have been sold out'))
        self.event.tickets.append(self.id)
        if number and number not in created_tickets:
            self.id = number
        created_tickets.append(self.id)

    def getprice(self):
        return self.price

    def __str__(self):
        return f'''id - {self.id}  price - {self.price}
Thank you for purchase! Enjoy the event!
________________________________________________________'''


class RegularTicket(Ticket):
    def __init__(self, event, number=None):
        super().__init__(event, number)
        info = {
            "name" : "Regular",
            "id" : str(self.id),
            "price" : self.price,
            "event" : self.event.name,
        }
        data['tickets'].append(info)
        with open("tickets.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    def __str__(self):
        out =  """________________________________________________________\nRegular ticket\n"""
        out += super().__str__()
        return out


class AdvanceTicket(Ticket):
    def __init__(self, event, number=None):
        super().__init__(event, number)
        self.price = int(self.price * 0.6)
        info = {
            "name": "Advance",
            "id": str(self.id),
            "price": self.price,
            "event": self.event.name,
        }
        data['tickets'].append(info)
        with open("tickets.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    def __str__(self):
        out = """________________________________________________________\nAdvance ticket\n"""
        out += super().__str__()
        return out


class StudentTicket(Ticket):
    def __init__(self, event, number=None):
        super().__init__(event, number)
        self.price = int(self.price * 0.5)
        info = {
            "name": "Student",
            "id": str(self.id),
            "price": self.price,
            "event": self.event.name,
        }
        data['tickets'].append(info)
        with open("tickets.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    def __str__(self):
        out = """________________________________________________________\nStudent ticket\n"""
        out += super().__str__()
        return out


class LateTicket(Ticket):
    def __init__(self, event, number=None):
        super().__init__(event, number)
        self.price = int(self.price * 1.1)
        info = {
            "name": "Late",
            "id": str(self.id),
            "price": self.price,
            "event": self.event.name,
        }
        data['tickets'].append(info)
        with open("tickets.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    def __str__(self):
        out = """________________________________________________________\nLate ticket\n"""
        out += super().__str__()
        return out


class Event:
    def __init__(self, name, date, places, price):
        self.name = name
        self.date = date
        self.places = places
        self.price = price
        self.tickets = []


def manager(evs):
    while True:
        personal_id = None
        out = ''
        for i in range(len(evs)):
            out += str(i+1) + '. ' + evs[i].name + '\n'
        print('Hi! Choose an event:')
        print(out.rstrip())
        ans = input()
        try:
            chosen = evs[int(ans) - 1]
        except IndexError:
            print('Wrong number')
            continue
        print('Will you enter your own id?\n1.No\n2.Yes')
        ans = input()
        if ans == '2':
            personal_id = input('Enter your own id (it will be replaced by default if it is already taken): ')
        print('Choose a ticket:\n1.Adult\n2.Student')
        ans = input()
        if ans == '2':
            if personal_id:
                new_ticket = StudentTicket(chosen, personal_id)
            else:
                new_ticket = StudentTicket(chosen)
        else:
            now = datetime.now()
            d60 = timedelta(days=60)
            d10 = timedelta(days=10)
            if chosen.date - d60 > now:
                if personal_id:
                    new_ticket = AdvanceTicket(chosen, personal_id)
                else:
                    new_ticket = AdvanceTicket(chosen)
            elif chosen.date - d10 < now:
                if personal_id:
                    new_ticket = LateTicket(chosen, personal_id)
                else:
                    new_ticket = LateTicket(chosen)
            else:
                if personal_id:
                    new_ticket = RegularTicket(chosen, personal_id)
                else:
                    new_ticket = RegularTicket(chosen)
        print('It costs', new_ticket.price)
        print(new_ticket)
        if input('Buy more?(Y/N): ').lower() != 'y':
            break

av_evs = []
for event in data['events']:
    ticks = []
    for ticket in data['tickets']:
        if ticket['event'] == event['name']:
            ticks.append(ticket['id'])
    t = event['date'].split('-')
    y = int(t[0])
    m = int(t[1])
    d = int(t[2])
    ev = Event(event['name'], datetime(y, m, d), event['places'], event['price'])
    ev.tickets = ticks
    av_evs.append(ev)


manager(av_evs)