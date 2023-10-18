num1 = float(input())
num2 = float(input())
op = input()
if op == '+':
    res = num1+num2
    print(res)
elif op == '-':
    res = num1-num2
    print(res)
elif op == '*':
    res = num1*num2
    print(res)
elif op == '/' or op == 'div' or op == 'mod':
    if num2 == 0:
        print('Деление на 0!')
    else:
        if op == '/':
            res = num1/num2
            print(res)
        elif op == 'div':
            res = num1//num2
            print(res)
        else:
            res = num1%num2
            print(res)
elif op == 'pow':
    res = num1**num2
    print(res)