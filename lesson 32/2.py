from string import ascii_lowercase as asc
a = input().lower()
b = input().lower()

w1 = 0


for i in range(len(a)):
    if a[i] != b[i]:
        if asc.index(a[i]) > asc.index(b[i]):
            w1 = 1
            break
        else:
            w1 =-1
            break
print(w1)