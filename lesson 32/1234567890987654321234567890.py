ss_ssr = input().split("+")
ss_ssr = sorted(ss_ssr)
leng = len(ss_ssr) - 2
a = []
b = ""

for i in range(len(ss_ssr)):
    a.append(ss_ssr[i])
    if i <= leng:
        a.append("+")

for i in range(len(a)):
    b += a[i]

print(b)