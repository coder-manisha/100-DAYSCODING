def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
# pi is the partition return index of pivot
        pi = partition(arr, low, high)

# Recursion calls for smaller elements
# and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)




arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

quickSort(arr, 0, n - 1)

for val in arr:
    print(val, end=" ")