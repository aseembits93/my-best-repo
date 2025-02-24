def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j],
                )  # Swapping without a temp variable
                swapped = True
        if not swapped:  # No swaps means the array is already sorted
            break
    return arr
