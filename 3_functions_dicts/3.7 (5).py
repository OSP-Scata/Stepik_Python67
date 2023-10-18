f_n = 'dataset_3380_5.txt'
with open(f_n, 'r') as f_o:
    lines = f_o.readlines()

school = {"1": [0, 0], "2": [0, 0], "3": [0, 0], "4": [0, 0], "5": [0, 0], "6": [0, 0], "7": [0, 0], "8": [0, 0],
          "9": [0, 0], "10": [0, 0], "11": [0, 0]}
for line in lines:
    pupil = line.split('\t')
    n = school[pupil[0]]
    n[0] += int(pupil[2])
    n[1] += 1
    school[pupil[0]] = n
for k, v in school.items():
    print(k + " ", end='')
    if v[0] == 0 and v[1] == 0:
        print('-')
    else:
        print(str(v[0] / v[1]))