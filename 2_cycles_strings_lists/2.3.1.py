a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t', *range(c,d+1), sep='\t', end='\t')
for i in range(a, b+1):
    print()
    print(i, end='\t')
    for k in range(d-c+1):
        print(i*(c+k), end='\t')