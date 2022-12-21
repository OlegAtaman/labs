from abc import ABC, abstractmethod


class BasicCourse(ABC):
    @abstractmethod
    def __init__(self, title, students, start_date):
        self.title = title
        self.students = students
        self.start_date = start_date

    @abstractmethod
    def __str__(self):
        out = f'Title: {self.title}\nStudents:\n'
        if len(self.students):
            for i in range(len(self.students)):
                out += f'{i + 1}. {self.students[i]}\n'
        else:
            out += 'None'
        out += f'Start date: {self.start_date}'
        return out


class LocalCourse(BasicCourse):
    def __init__(self, title, students, start_date):
        super().__init__(title, students, start_date)
        self.location = 'Kyiv Politechnic Institute'

    def __str__(self):
        return super().__str__() + '\nLocation: ' + self.location


class OffsiteCourse(BasicCourse):
    def __init__(self, title, students, start_date, location):
        super().__init__(title, students, start_date)
        self.location = location

    def __str__(self):
        return super().__str__() + '\nLocation: ' + self.location


class Teacher:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        if isinstance(course, OffsiteCourse) or isinstance(course, LocalCourse):
            if course not in self.courses:
                self.courses.append(course)

    def exit_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def __str__(self):
        out = self.name + '\n'
        if len(self.courses):
            out += 'Teacher of:\n'
            for course in self.courses:
                out += course.title + '\n'
        else:
            out += 'Teaches nothing now'
        return out.rstrip()


class CourseFactory:
    teachers = []
    courses = []

    def run(self):
        while True:
            print('=== MAIN MENU ===')
            print('1. Existing teachers\n2. New teacher\n3. Existing courses\n4. New course\n5. Quit')
            answer = input('Answer: ')
            if answer == '1':
                print(self.get_teachers())
                if self.teachers:
                    print('Print number to select teacher or 0 to go back to menu')
                    answer = input('Answer: ')
                    if answer != '0':
                        try:
                            index = int(answer) - 1
                            selected = self.teachers[index]
                            self.manage_teacher(selected)
                        except ValueError:
                            print('Unknown command')
                        except IndexError:
                            print('Wrong number')
            elif answer == '2':
                self.create_teacher()
            elif answer == '3':
                print(self.get_courses())
                if self.courses:
                    print('Print number to select course or 0 to go back to menu')
                    answer = input('Answer: ')
                    if answer != '0':
                        try:
                            index = int(answer) - 1
                            selected = self.courses[index]
                            print(selected)
                        except ValueError:
                            print('Unknown command')
                        except IndexError:
                            print('Wrong number')
            elif answer == '4':
                self.create_course()
            elif answer == '5':
                break
            else:
                print('Unknown command')

    def get_teachers(self):
        out = 'Teachers:\n'
        if self.teachers:
            for i in range(len(self.teachers)):
                out += f'{i + 1}. {self.teachers[i].name}\n'
        else:
            out += 'None'
        return out.rstrip()

    def get_courses(self):
        out = 'Courses:\n'
        if self.courses:
            for i in range(len(self.courses)):
                out += f'{i + 1}. {self.courses[i].title}\n'
        else:
            out += 'None'
        return out.rstrip()

    def manage_teacher(self, teacher):
        while True:
            print(f'Selected teacher:')
            print(teacher)
            print('1. Add course\n0. Go to main menu')
            answer = input('Answer: ')
            if answer == '1' and self.courses:
                print(self.get_courses())
                print("Enter number to add to teacher's courses or 0 to cancel")
                ans = input('Answer: ')
                if ans != '0':
                    try:
                        selected = self.courses[int(ans)-1]
                        teacher.add_course(selected)
                    except ValueError:
                        print('Unknown command')
                    except IndexError:
                        print('Wrong number')
            elif answer == '1':
                print('There is no available courses')
            elif answer == '0':
                break
            else:
                print('Unknown command')

    def create_teacher(self):
        name = input("Enter teacher's name: ")
        teacher = Teacher(name)
        self.teachers.append(teacher)
        self.manage_teacher(teacher)

    def create_course(self):
        title = input('Enter title: ')
        std_input = input('Enter students names splited by comma: ')
        students = std_input.split(',')
        for i in range(len(students)):
            students[i] = students[i].strip()
        date = input('Enter date of course start: ')
        location = input('Enter course location (skip to set default): ')
        if location:
            new_course = OffsiteCourse(title, students, date, location)
        else:
            new_course = LocalCourse(title, students, date)
        self.courses.append(new_course)
        print('Course created')


my_factory = CourseFactory()
my_factory.run()
