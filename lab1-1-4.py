import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)

args = parser.parse_args()


def solution(W, w):
    bars = len(w)
    capacity = {}
    for c in range(W+1):
        capacity[(0, c)] = 0
    for i in range(1, bars+1):
        for j in range(W+1):
            if w[i-1] <= j:
                capacity[(i, j)] = max(capacity[(i-1, j)], w[i-1] + capacity[(i-1, j-w[i-1])])
            else:
                capacity[(i, j)] = capacity[(i-1, j)]
    return capacity[(bars, W)]


print(solution(args.W, args.w))
