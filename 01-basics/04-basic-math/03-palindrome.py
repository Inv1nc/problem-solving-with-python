n = int(input())
temp = n
rev = 0

while(n > 0):
    ld = n % 10
    n = n // 10
    rev = (rev * 10) + ld

if temp == rev:
    print("true")
else:
    print("false")
