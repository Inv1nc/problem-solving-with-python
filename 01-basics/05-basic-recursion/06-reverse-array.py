def reverse(i, arr, n):
    if i >= n // 2:
        return

    temp = arr[n-1-i]
    arr[n-1-i] = arr[i]
    arr[i] = temp

    return reverse(i+1, arr, n)

def main():
    n = list(map(int, input().split(' ')))
    reverse(0, n, len(n))
    print(n)

if __name__ == "__main__":
    main()

