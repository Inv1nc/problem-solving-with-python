arr = list(map(int, input().split(' ')))

hash = [0] * 13

# precompute
for i in range(len(arr)):
    hash[arr[i]] += 1

q = int(input())

for _ in range(q):
    i = int(input())
    print(hash[i])
