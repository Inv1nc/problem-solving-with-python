def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy data into temp arrays
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left    # start update from left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


if __name__ == "__main__":
    arr = list(map(int, input().split(' ')))
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
