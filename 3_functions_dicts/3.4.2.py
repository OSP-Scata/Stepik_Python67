filename = "dataset_3363_3.txt"
with open(filename, 'r') as f_o:
    lines = f_o.readlines()
l = []
for line in lines:
    l += line.split()
for i in range(len(l)):
    l[i] = l[i].lower()
d = {}
for word in l:
    if word in d:
        n = d[word]
        n[0] += 1
        d[word] = [n[0]]
    else:
        n = 1
        d[word] = [n]
print(d)
n = max(d.values())
s = []
i = 0
for key, value in d.items():
    if value == n:
        s.append(key)
s_min = min(s)
dir_1 = {}
f = open("file.txt", 'w')
f.write(s_min + ' ' + str(n[0]))
f.close()