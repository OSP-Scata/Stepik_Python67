a = []
n = input()
while n != "end":
    s = n.split()
    ar = []
    for i in s:
        ar.append(int(i))
    a.append(ar)
    n = input()
size_2 = len(a[0])
size_1 = len(a)
ar_1 = []
ar = []
i = 0
while i < size_1:
    j = 0
    ar_1 = []
    while j < size_2:
        s = 0
        if i == 0:
            s += a[size_1 - 1][j]
        elif i == 0 and size_1 == 1:
            s += a[i][j]
        else:
            s += a[i - 1][j]
        if size_1 != 1 and i == size_1 - 1:
            s += a[0][j]
        elif size_1 == 1 and i == 0:
            s += a[i][j]
        else:
            s += a[i + 1][j]
        if j == 0:
            s += a[i][size_2 - 1]
        elif j == 0 and size_2 == 1:
            s += a[i][j]
        else:
            s += a[i][j - 1]
        if size_2 != 1 and j == size_2 - 1:
            s += a[i][0]
        elif size_2 == 1 and j == 0:
            s += a[i][j]
        else:
            s += a[i][j + 1]
        ar_1.append(s)
        j += 1
    ar.append(ar_1)
    i += 1
for i in range(size_1):
    for j in range(size_2):
        print(ar[i][j], end=' ')
    print()
