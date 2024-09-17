def fibinocci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibinocci(n-1) + fibinocci(n-2)

if __name__ == "__main__":
    n = int(input())
    print(fibinocci(n))
