def bubblesort(arr):
    for i in range(len(arr)):
        for  j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


d= [4,3,1,6,24,0,-2]
bubblesort(d)
print(d)