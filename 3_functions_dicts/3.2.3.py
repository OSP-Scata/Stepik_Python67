n = int(input())
d = {}
while n > 0:
    num = int(input())
    if num in d:
        print(d[num][0])
        n -= 1
    else:
        d[num] = [f(num)]
        print(d[num][0])
        n -= 1
