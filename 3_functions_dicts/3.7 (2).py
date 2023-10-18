def make_list(line):
    mylist = []
    for i in line:
        mylist.append(i)
    return mylist


def cipher(line, value, mykey):
    for l in line:
        i = 0
        while i < len(value):
            if l == value[i]:
                print(mykey[i], end='')
                break
            i += 1


line_1 = input()
line_2 = input()
line_3 = input()
line_4 = input()
letters = make_list(line_1)
key = make_list(line_2)
cipher(line_3, letters, key)
print()
cipher(line_4, key, letters)
