def print_num(i, n):
    if i > n:
        return

    print(i)
    print_num(i + 1, n)

def main():
    n = int(input())
    print_num(1, n)

if __name__ == "__main__":
    main()
