import argparse


def check(string):
    if string[0] in ['+', '-']:
        return False
    prev = ''
    for c in string:
        if not c.isdigit() and not prev.isdigit():
            return False
        elif c in ['*', '/', '%', '^']:
            return False
        prev = c
    return True


parser = argparse.ArgumentParser()

parser.add_argument("expr", type=str)

lab = parser.parse_args()

try:
     if check(lab.expr):
        print('True,', eval(lab.expr))
     else:
        print('False, None')
except:
    print('False, None')
