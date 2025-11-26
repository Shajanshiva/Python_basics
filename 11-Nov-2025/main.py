# task 1
def two_zero(a):
    b = 0
    c = []
    for i in range(0, len(a), 1):
        if a[i] == 0:
            b = b + i
            break
    for i in range(b+1, len(a), 1):
        if a[i] == 0:
            break
        else:
            c.append(a[i])
    print(c)

two_zero([3,0,4,7,2,0,4])
            
            
# task 2
def sec_large_num(num):
    b = 0
    c = 0
    d = 0
    for i in range(0, len(num), 1):
        if num[i] > b:
            c = i
            b = num[i]
    del num [c]
    for i in range(0, len(num), 1):
        if num[i] > d:
            d = num[i]

    print(d)
    
sec_large_num([4,9,1,7,3])

# task 3
def remove_duplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
remove_duplicates([1,2,3,1,2,4])