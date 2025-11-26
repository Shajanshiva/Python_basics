# task 1
def k_position(nums, k):
    if len(nums) == 0 :
        print("invalid input")
    else:
        for i in range(-k, len(k), 1):
            print(nums[i])

k_position([6,4,8,2,9,4], 3)


# task 2
def small_word(word):
    a = word.split( )
    b = a[0]
    if len(word) == 0:
        print("invalid input")
    else:
        for i in a:
            if len(i) < len(b):
                b = i
        print(b)
            
small_word("Python is super powerful")


# task 3
def increase(num):
    a = num[0]
    b =""
    if len(num) == 0:
        print("invalid input")
    else:
        for i in range(1, len(num), 1):
            if num[i] > a:
                b = "true"
            else:
                b = "false"
                break
        print(b)
            
increase([0, 1, 3, 5, 7])
increase([8, 3, 4, 6, 10])
increase([2, 2, 7, 9])


# task 4
def lst_num(nums, value):
    a =[]
    if len(nums) == 0:
        print("invalid input")
    else:
        for i in range(len(nums)-value, len(nums), 1):
            a.append(nums[i])
            
        for i in range(0, len(nums)-value, 1):
            a.append(nums[i])
            
        print(a)
            
    
lst_num([4,6,9,2,3,11], 2)
lst_num([0,3,5,8,5,2,7], 4)


# task 5
def lst_num(nums, k):
    a =[]
    b = 0
    if len(nums) == 0:
        print("invalid input")
    else:
        for i in range(0, len(nums), 1):
            if nums[i] == k:
                a.append(i)
            else:
                b += 1
        if len(nums) == b:
            print("Not Found")
        else:
            print(a)
        
        
               
lst_num([4,2,7,2,9,3,2,8], 2) 
lst_num([10,55,17,29,3], -45)
lst_num([10,5,7,17,9,7], 7)


# task 6
def reverse_order(nums):
    a =[]
    if len(nums) == 0:
        print(nums)
    else:
        for i in range(len(nums)-1, -1, -1):
            a.append(nums[i])
        print(a)
        
reverse_order([1, 3, 7, 8, 9])
reverse_order([3, 8, 4, 0, 1])
reverse_order([])


# task 7
def upper_case(word):
    a = ["Q","W","E","R","T","Y","U","I","O","P","L","K","J","H","G","F","D","S","A","Z","X","C","V","B","N","M"]
    b = 0
    if len(word) == 0:
        print("invalid input")
    else:
        for el in word:
            for i in a:
                # print(i)
                if el == i:
                    b += 1
                    # print(b)
        print(b)
        
upper_case("HelloWorld")


# task 8
def swapped(word):
    a = word.split()
    b = "" 
    for i in range(len(a)-1, -1, -1):
        b = b + " " + a[i]
    print(b)
swapped("apple and banana")


#task 9
def fact(num):
    a = 1
    b = []
    if len(num) == 0:
        print("Invalid input")
    else:
        for i in num:
            for j in range(i, 0, -1):
                a = j * a
            b.append(a)
            a = 1
            
        print(b)

fact([3, 5, 1, 4])


#task 10
def subarray(num):
    count = 0
    if len(num) == 0:
        print("Invalid input")
    else:
        for i in range(0, len(num), 1):
            s = 0
            p = 1
            for j in range(i, len(num), 1):
                s += num[j]
                p *= num[j]
                if s == p:
                    count += 1
        print(count)
                
            
            
subarray([1,2,3])


#task 11

def palindrom(word):
    if len(word) == 0:
        print("Invalid input")
    else:
        for k in word:
            print(k)
        for i in range(0, len(word), 1):
            for j in range(i, len(word), 1):
                temp = word[i:j + 1]
                if temp == temp[::-1]:
                    if len(temp) > 1:
                    print(temp)
                
palindrom("racecar")
        