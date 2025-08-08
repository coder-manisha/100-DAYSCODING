def right_rotate(lst, n):
    size = len(lst)
    n = n % size

    for r in range(n):
        last = lst[size - 1]
        for i in range(size - 1, 0, -1):
            lst[i] = lst[i - 1]
        lst[0] = last

    return lst
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter number of right rotations: "))
rotated = right_rotate(arr, n)
print("Rotated list:", rotated)
