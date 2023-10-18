with open('dataset_3363_2.txt', 'r') as infile:
    string = infile.readline().strip()
result = ''
for i in range(len(string)):
    if not string[i].isdigit():
        j = i + 1
        counter = ''
        while string[j].isdigit():
            counter += string[j]
            if j + 1 < len(string):
                j += 1
            else:
                break
        counter = int(counter)
        result += string[i] * counter
with open('outfile.txt', 'w') as outfile:
    outfile.write(result)