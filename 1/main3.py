import argparse

parser = argparse.ArgumentParser()

parser.add_argument("expression")

lab = parser.parse_args()


def check(string):
    prev = ''
    for c in string:
        if not c.isdigit() and not prev.isdigit():
            return False
        elif c == '*' or c == '/':
            return False
        prev = c
    return True


try:
     if check(lab.expression):
        print('True,', eval(lab.expression))
     else:
        print('False, None')
except:
    print('False, None')
