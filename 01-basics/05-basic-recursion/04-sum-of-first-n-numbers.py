def print_sum(n):
    if n == 0:
        return 0
    return n + print_sum(n - 1)

if __name__ == "__main__":
    n = int(input())
    print(print_sum(n))
