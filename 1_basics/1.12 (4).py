type = input()
s = None
if type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
elif type == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = float(a*b)
elif type == 'круг':
    r = int(input())
    s = 3.14*r**2
print(s)