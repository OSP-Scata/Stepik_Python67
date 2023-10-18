num = int(input())
if 10 < num%100 < 20:
    print(num, 'программистов')
else:
    if num%10 == 1:
        print(num, 'программист')
    elif 2 <= num%10 <= 4:
        print(num, 'программиста')
    else:
        print(num, 'программистов')