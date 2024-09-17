def print_num(i, n):
    if i < 1:
        return

    print(i)
    print_num(i - 1, n)

def main():
    n = int(input())
    print_num(n, n)

if __name__ == "__main__":
    main()
