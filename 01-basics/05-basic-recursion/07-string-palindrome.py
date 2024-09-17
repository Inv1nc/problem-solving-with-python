def is_palindrome(i, str, n):
    if i >= n//2:
        return True

    if str[i] != str[n-i-1]:
        return False

    return is_palindrome(i + 1, str, n)


def main():
    str = input("")
    print(is_palindrome(0, str, len(str)))

if __name__ == "__main__":
    main()
