#printing d
s = input('enter the value: ')
s1 = {}
for i in s:
    if i in s1:
        s1[i] = s1[i]+1
    else:
        s1[i]=1
print(s1)
for char,count in s1.items():
    if count > 1:
        print(f'{char} appeared {count} times')
