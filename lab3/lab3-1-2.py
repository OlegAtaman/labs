from datetime import datetime


month_days = {
    1 : 31, 2 : 28, 3 : 31, 4 : 30,
    5 : 31, 6 : 30, 7 : 31, 8 : 31,
    9 : 30, 10 : 31, 11 : 30, 12 : 31
}

class Day:
    def __init__(self, number):
        if isinstance(number, int):
            self.day = number
        else:
            raise TypeError('Day must be integer')

    def __str__(self):
        return str(self.day)


class Month:
    def __init__(self, number):
        if isinstance(number, int):
            self.month = number
        else:
            raise TypeError('Month must be integer')

    def __str__(self):
        return str(self.month)


class Year:
    def __init__(self, number):
        if isinstance(number, int):
            self.year = number
        else:
            raise TypeError('Year must be integer')

    def __str__(self):
        return str(self.year)


class Date:
    def __init__(self, day, month, year):
        if not isinstance(day, Day) or not isinstance(month, Month) or not isinstance(year, Year):
            raise TypeError('Day, month and year must be Day(), Month() and Year() objects.')

        self.day = day
        self.month = month
        self.year = year

        while self.month.month < 1:
            self.year.year -= 1
            self.month.month += 12

        while self.day.day < 1:
            self.month.month -= 1
            if self.month.month < 1:
                self.month.month += 12
                self.year.year -= 1
            self.day.day += month_days.get(self.month.month)

        while self.month.month > 12:
            self.year.year += 1
            self.month.month -= 12

        while self.day.day > month_days.get(self.month.month):
            self.day.day -= month_days.get(self.month.month)
            self.month.month += 1
            if self.month.month > 12:
                self.month.month = 1
                self.year.year += 1

        self.absolute = self.year.year * 365
        for i in range(1, self.month.month + 1):
            self.absolute += month_days.get(i)
        self.absolute += self.day.day

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'

    def __iadd__(self, other):
        if isinstance(other, Day):
            return Date(Day(self.day.day + other.day), self.month, self.year)
        if isinstance(other, Month):
            return Date(self.day, Month(self.month.month + other.month), self.year)
        if isinstance(other, Year):
            return Date(self.day, self.month, Year(self.year.year + other.year))
        if isinstance(other, Date):
            return Date(Day(self.day.day + other.day.day), Month(self.month.month + other.month.month),
                        Year(self.year.year + other.year.year))

    def __isub__(self, other):
        if isinstance(other, Day):
            return Date(Day(self.day.day - other.day), self.month, self.year)
        if isinstance(other, Month):
            return Date(self.day, Month(self.month.month - other.month), self.year)
        if isinstance(other, Year):
            return Date(self.day, self.month, Year(self.year.year - other.year))
        if isinstance(other, Date):
            return Date(Day(self.day.day - other.day.day), Month(self.month.month - other.month.month),
                        Year(self.year.year - other.year.year))

    def __lt__(self, other):
        if isinstance(other, Date):
            if self.absolute >= other.absolute:
                return False
            return True

    def __gt__(self, other):
        if isinstance(other, Date):
            if self.absolute <= other.absolute:
                return False
            return True

    def __le__(self, other):
        if isinstance(other, Date):
            if self.absolute > other.absolute:
                return False
            return True

    def __ge__(self, other):
        if isinstance(other, Date):
            if self.absolute < other.absolute:
                return False
            return True

    def __eq__(self, other):
        if isinstance(other, Date):

            if self.absolute == other.absolute:
                return True
            return False

    def __ne__(self, other):
        if isinstance(other, Date):
            if self.absolute != other.absolute:
                return True
            return False


class Calendar:
    def __init__(self, days):
        today = Date(Day(datetime.now().day), Month(datetime.now().month), Year(datetime.now().year))
        self.calendar = {}
        self.calendar.update({today.absolute + 1 : ''})
        for day in range(1, days):
            today += Day(1)
            self.calendar.update({today.absolute: ''})

    def __str__(self):
        out = ''
        for date, plan in self.calendar.items():
            out += f'Plans for {Date(Day(date), Month(0), Year(0))}:\n' + plan
            if plan:
                out += '\n'
        return out

    def add_plan(self, date, plan):
        if not isinstance(date, Date):
            raise TypeError('Date must be Date() object in range of calendar.')
        if isinstance(self.calendar.get(date.absolute), str):
            if len(self.calendar.get(date.absolute)) > 0:
                self.calendar[date.absolute] += '\n'
            self.calendar[date.absolute] += plan
        else:
            raise ValueError('Date must be Date() object in range of calendar.')

    def remove_plan(self, date, plan):
        if not isinstance(date, Date):
            raise TypeError('Date must be Date() object in range of calendar.')
        if isinstance(self.calendar.get(date.absolute), str):
            if plan in self.calendar.get(date.absolute):
                if self.calendar.get(date.absolute).index(plan) != 0:
                    self.calendar[date.absolute] = self.calendar[date.absolute].replace('\n' + plan, '')
                else:
                    self.calendar[date.absolute] = self.calendar[date.absolute].replace(plan, '')
        else:
            raise ValueError('Date must be Date() object in range of calendar.')

# def get_date_by_event(event, calendar):
#     dates = [i for i in calendar.calendar if calendar.calendar[i] == event]
#     if dates:
#        return Date(Day(dates[0]), Month(0), Year(0))
#     else:
#         raise ValueError('There is no such event')

c = Calendar(7)
c.add_plan(Date(Day(5), Month(12), Year(2022)), 'Work on a python project')
c.remove_plan(Date(Day(5), Month(12), Year(2022)), 'Work on a python project')
date1 = Date(Day(3), Month(12), Year(2022))
c.add_plan(date1, 'Work on my math homework')
date1 += Day(3)
c.add_plan(date1, 'Finish my math homework')
print(c)