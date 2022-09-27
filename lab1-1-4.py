import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs="+")

lab = parser.parse_args()

capacity = lab.W
weight = lab.w

sums = []


def knapsack(capacity, weight, now=[]):
    cur_sum = sum(now)
    if cur_sum <= capacity:
        sums.append(cur_sum)
    for i in range(len(weight)):
        n = weight[i]
        remaining = weight[i+1:]
        knapsack(capacity, remaining, now+[n])


knapsack(capacity, weight)
print(max(sums))
