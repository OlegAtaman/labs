import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("operation", type=str)
parser.add_argument('num', type=float, nargs='+')

lab = parser.parse_args()

try:
    if hasattr(operator, lab.operation):
        act = getattr(operator, lab.operation)
        print(act(*lab.num))
    else:
        func = getattr(math, lab.operation)
        print(func(*lab.num))
except Exception:
    print('Something wrong')
