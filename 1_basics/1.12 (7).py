ticket = input()
ticket = int(ticket)
sum1 = ticket//100000 + (ticket//10000)%10 + (ticket//1000)%10
sum2 = (ticket//100)%10 + (ticket//10)%10 + ticket%10
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')