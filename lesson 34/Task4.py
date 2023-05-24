import random as r
from string import ascii_uppercase as asc

string = ""
n = int(input())
for i in range(n):
    a = r.randint(0,25)
    string = string + (asc[a])

s = set(string)

print(string)
print(s)

uni = ""

for bukva in s:
    uni += bukva

print(uni)
