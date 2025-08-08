def delete(lst,index):
    if index < 0 or index >= len(lst):
        print("Invalid index")
        return lst
    new_list = [0] * (len(lst) - 1)
    j = 0
    for i in range(len(lst)):
        if i == index:
            continue
        new_list[j] = lst[i]
        j += 1

    return new_list

l = [10, 20, 30, 40, 50]
idx = int(input("Enter index to delete: "))
result = delete(l, idx)
print("List after deletion:", result)
