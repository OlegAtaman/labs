import argparse

def calculate(num1, num2, act):
    if act == '+':
        result = num1 + num2
    elif act == '-':
        result = num1 - num2
    elif act == '*':
        result = num1 * num2
    elif act == '/':
        result = num1 / num2
    return result

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integer1', metavar='N', type=int, help='an integer for the accumulator')
parser.add_argument('action', nargs='?', const=sum)
parser.add_argument('integer2', metavar='N', type=int, help='an integer for the accumulator')

args = parser.parse_args()
print(calculate(args.integer1, args.integer2, args.action))