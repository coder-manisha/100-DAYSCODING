def binarySearch(arr,low,high,val):
    if low <= high:
        mid = (low +high)// 2
        if arr[mid] == val:
            return mid
        elif arr[mid]>val:
            return(binarySearch(arr,low,mid-1,val))
        else:
            return(binarySearch(arr,mid+1,high,val))
    else:
        return -1

arr = [2,3,5,2,4,124,24]
arr.sort()
val = 2
a = binarySearch(arr,0,len(arr)-1,val)
print('element is present at index' ,a)