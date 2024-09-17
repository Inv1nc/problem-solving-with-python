def print_factorial(n):
    if n == 0:
        return 1
    return n * print_factorial(n - 1)

if __name__ == "__main__":
    n = int(input())
    print(print_factorial(n))
