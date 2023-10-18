a = int(input())
b = int(input())
x = a
y = b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print((x*y)//a)