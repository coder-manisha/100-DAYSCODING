def merge(l1,l2):
    l1.sort()
    l2.sort()
    i  = 0
    j = 0
    merged = []
    while i<len(l1) and j<len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i = i+1
        else:
            merged.append(l2[j])
            j = j+1
    while i < len(l1):
        merged.append(l1[i])
        i = i+1
    while j < len(l2):
        merged.append(l2[j])
        j = j+1
    return merged
l1 = [10,20,-1,22]
l2 = [12,22,11]
print(merge(l1,l2))