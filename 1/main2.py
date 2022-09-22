import argparse
import operator

parser = argparse.ArgumentParser()

parser.add_argument("function")
parser.add_argument('int1', type=int)
parser.add_argument('int2',  type=int)

lab = parser.parse_args()

try:
    func = getattr(operator, lab.function)
except:
    print('Wrong function')

print(func(lab.int1, lab.int2))
