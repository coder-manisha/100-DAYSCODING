def left_rotate(lst, n):
    size = len(lst)
    n = n % size

    for r in range(n):
        first = lst[0]
        for i in range(size - 1):
            lst[i] = lst[i + 1]
        lst[size - 1] = first

    return lst

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter number of left rotations: "))
rotated = left_rotate(arr, n)
print("Rotated list:", rotated)
