class Student:
    def __init__(self, name, surname, booknum, grades):
        self.name = name
        self.surname = surname
        self.booknum = booknum
        self.grades = grades

    def get_avg(self):
        return sum(self.grades) / len(self.grades)

class Group:
    def __init__(self, students):
        self.__students = []
        if len(students) <= 20:
            self.__students = students
        else:
            print('More than 20 students')

    def print_top(self):
        if self.__students:
            top_students = sorted(self.__students, key=lambda x: x.get_avg(), reverse=True)[:5]
            print('Top five students:')
            for i in range(len(top_students)):
                print(f'{i + 1}. {top_students[i].name} {top_students[i].surname} - {top_students[i].get_avg()} points')


stud1 = Student('Billy', 'Herrington', 'HFDKEN', [5, 4, 5, 5])
stud2 = Student('Van', 'Darkholme', 'FDDSGD', [5, 5, 4, 5])
stud3 = Student('Semen', 'Vovchyk', 'DDWSDX', [4, 4, 3, 3])
stud4 = Student('XAEA-12', '', 'EFFSEC', [5, 5, 3, 4])
stud5 = Student('Bot', 'Henry', 'EKJFNC', [3, 5, 3, 4])
stud6 = Student('Lackof', 'Imagination', 'DEWDDD', [4, 3, 4, 4])


group1 = Group([stud1, stud2, stud3, stud4, stud5, stud6])
group1.print_top()
