import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs="+")
lab = parser.parse_args()

evrvar = []


def bagpack(capacity, weight, now=[]):
    weightn = sum(now)
    if weightn <= capacity:
        evrvar.append(weightn)
    for i in range(len(weight)):
        n = weight[i]
        left = weight[i+1:]
        bagpack(capacity, left, now+[n])


bagpack(lab.W, lab.w)
print(max(evrvar))
