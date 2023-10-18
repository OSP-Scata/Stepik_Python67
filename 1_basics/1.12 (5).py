a = int(input())
b = int(input())
c = int(input())
max = a
min = a
rest = a
if (a >= b) and (a>=c):
    if b <= c:
        min = b
        rest = c
    else:
        min = c
        rest = b
elif (b>=a) and (b>=c):
    max = b
    if a >= c:
        min = c
    else:
        rest = c
else:
    max = c
    if a >= b:
        min = b
    else:
        rest = b
print(max)
print(min)
print(rest)