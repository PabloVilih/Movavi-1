import random as r

s = set()

for i in range(10):
    s.add(r.randint(0,15))

x = list(s)
x.sort()

print(x)