a = int(input())
b = int(input())

while a > 0 and b > 0:
    if a > b:
        a = a % b
        b = b
    else:
        b = b % a
        a = a

if a == 0:
    print(b)
else:
    print(a)
