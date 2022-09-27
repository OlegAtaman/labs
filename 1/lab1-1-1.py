import argparse


def calculate(int1, int2, operation):
    if operation == '+':
        print(int1 + int2)
    elif operation == '-':
        print(int1 - int2)
    elif operation == '*':
        print(int1 * int2)
    elif operation == '/':
        try:
            print(int1 / int2)
        except ZeroDivisionError:
            print('You can not divide by zero')
    else:
        print('Wrong action')


parser = argparse.ArgumentParser()

parser.add_argument('int1', type=int)
parser.add_argument('operation', type=str)
parser.add_argument('int2', type=int)

lab = parser.parse_args()

calculate(lab.int1, lab.int2, lab.operation)
