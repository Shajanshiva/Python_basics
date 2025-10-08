x = 5
y = 2
print (x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# step 1 : getting input from thr user
n = int(input("Enter a number"))
print(n)

# step 2 : condition check
if n%2==0:
    print("Even")
else:
    print("Odd")    


#finding leap year
n = int(input("Enter a four digit number"))

if n%4==0:
    print("It's leap year")
else:
    print("It's not a leap year")


#find another leap year
A = int(input("Enter the year in positive integer"))

if n%4==0:
    print("Y")
else:
    print("N")


#Finding division for 3 or 5
n = int(input("Enter a number"))
if n%3==0 or n%5==0:
    print("Divisible")
else:
    print("Not divisible")    

#check if the year falls within the 21st century 
A = int(input("enter a four digit number"))
print(A)
if A>=2001 and A<=2100:
    print("21st Century")
else:
    print("Not in 21st Century")


