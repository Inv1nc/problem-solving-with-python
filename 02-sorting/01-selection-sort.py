# taking array input
a = list(map(int, input().split(" ")))

for i in range(len(a) - 1):
    min = i

    # finding for the minimum
    for j in range(i, len(a)):
        if a[j] < a[min]:
            min = j

    # swap
    if min != i:
        a[i], a[min] = a[min], a[i]

print(a)
