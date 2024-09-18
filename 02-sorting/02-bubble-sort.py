a = list(map(int, input().split(" ")))

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):

        # moving greater element to right
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
