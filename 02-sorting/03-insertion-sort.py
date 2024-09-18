a = list(map(int, input().split(' ')))

for i in range(len(a)):
    j = i
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1

print(a)
