def remove_duplicates(char):
    c = ''
    for i in char:
        if i not in c:
            c = c + i
    return c
char = input("enter string: " )
a = remove_duplicates(char)
print(a)