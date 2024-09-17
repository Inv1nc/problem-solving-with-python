n = int(input())
temp = n
count = 0

while n > 0:
    n = n // 10
    count += 1


final  = temp
armstrong = 0

while temp > 0:
    ld = temp % 10
    temp = temp // 10
    armstrong = armstrong + (ld ** count)

if armstrong == final:
    print("true")
else:
    print("false")
