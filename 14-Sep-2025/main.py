#task 1
W = input("Enter a Weather Rainy or Sunny")
print(W)

if W == "Rainy":
    print("Bring Umberlla")
else:
    print("No needd umberlla")


#task 2
M1 = int(input("Enter mark1 "))
print(M1)
M2 = int(input("Enter a mark2 "))
print(M2)
M3 = int(input("Enter a mark3 "))
print(M3)

if M1 > 40 and M2 > 40 and M3 > 40:
    print("promoted")
else:
    print("Not promoted")


#task 3
D = input("Enter a day of the week ")
print(D)

if D == "Saturday" or D == "Sunday":
    print("Holiday")
else:
    print("Working Day")


#task 4
N = int(input("Enter a number"))
print(N)

if N >= 1:
    print("Positive")
elif N <= -1:
    print("Negative")
else:
    print("Zero")


#task 5
M = int(input("Enter a months from 1 to 12 "))
print(M)

if 3 <= M <= 5:
    print("Spring")
elif 6 <= M <= 8:
    print("Summer")
elif 9 <= M <= 11:
    print("Autumn")
elif M == 12 or 1 <= M <= 2:
    print("Winter")
else:
    print("Invalid Input")


#task 6
C = input("Enter a alphabet ")
print(C)

if C == "A" or C == "E" or C == "I" or C == "O" or C == "U":
    print("Vowel")
else:
    print("Consonant")