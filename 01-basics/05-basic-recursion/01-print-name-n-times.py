def print_name(i, n):
    if (i > n):
        return

    print("yay")
    print_name(i + 1, n)

def main():
    print_name(1, 5)

if __name__ == "__main__":
    main()
