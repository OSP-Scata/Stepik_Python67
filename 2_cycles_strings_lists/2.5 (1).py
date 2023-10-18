str = input()
sum = 0
numbers = str.split(' ')
for i in numbers:
    sum += int(i)
print(sum)