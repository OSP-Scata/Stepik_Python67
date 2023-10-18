def read_lines(n):
    lines = []
    while n != 0:
        lines.append(input())
        n -= 1
    return (lines)


n = int(input())
commands = read_lines(n)
position = [0, 0]
for command in commands:
    com = command.split(' ')
    side = com[0]
    steps = int(com[1])
    if side == 'север':
        position[1] += steps
    elif side == 'восток':
        position[0] += steps
    elif side == 'юг':
        position[1] -= steps
    elif side == 'запад':
        position[0] -= steps
print(str(position[0]) + " " + str(position[1]))
