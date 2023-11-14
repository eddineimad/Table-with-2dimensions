n = int(input("Type the first number: "))
p = int(input("Type the second number: "))

while p < 0 or p > 10 or n < 0 or n > 10:
    n = int(input("Type the first number between 0 and 10: "))
    p = int(input("Type the second number between 0 and 10: "))

t = []
k = 0

for i in range(0, n):
    l = []
    for j in range(0, p):
        k += 1
        l.append(k)
    t.append(l)

for i in range(0, n):
    for j in range(0, p):
        print(t[i][j])

for i in range(0, n):
    for j in range(0, p):
        if i % 2 != 0:
            print(t[i][p - 1 - j])
        else:
            print(t[i][j])