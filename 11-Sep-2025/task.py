#task 1
sum of the two numbers is divisible by 5 or not 
a = int(input("enter a number a"))
b = int(input("enter a number b"))
print(a,b)
A = a+b
print(A)
if A%5==0:
    print(1)
else:
    print(0)

#task 2
print yes if the number is a multiple of 7 else print no
a = int(input("Enter a number"))
if a%7==0:
    print("Yes")
else:
    print("No") 

#task 3
a = int(input("enter a number"))
print(a)
if a>500:
    print("Free Delivery")
    print("the total amount is",a)
else:
    print("Charged")
    x = (a+50)
    print("the total charged amount is",x)
   
#task 4
X = int(input("Enter a number"))
print(X)
if 100 >= X >= 80:
    print("A")
elif 60 <= X <= 79:
    print("B")
elif 50 <= X <= 59:
    print("C")
elif 40 <= X <=49:
    print("D")
else :
    print("Fail")  

#task 5
a = int(input("Enter a number a"))
print(a)
b = int(input("Enter a number b"))
print(b)
c = int(input("Enter a number c"))
print(c)

A = a+b
if A>c:
    print("Yes")
else:
    print("No")

#task 6
A = int(input("Enter a age"))
print(A)
if A<13:
    print("Child")
elif 13 <= A <= 19:
    print("Teen")
elif 20 <= A <= 59:
    print("Adult")
elif 60 <= A <= 100:
    print("Senior")
else:
    print("Invalid Input")
