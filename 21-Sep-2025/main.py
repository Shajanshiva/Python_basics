# task 1
N = int(input("Enter any number"))
print(N)
M = int(input("Enter any number"))
print(M)

if (N+M)%2==0:
    print("even")
else:
    print("odd")


#task 2
n = int (input("Enter a 2 digit positive number"))
print(n)

#seprating the digit
first_digit = n // 10
second_digit = n % 10

#caluclate the sum and product of the digit
m = first_digit + second_digit
j = first_digit * second_digit

#checking the coondition
if m + j == n:
    print("Great")
else:
    print("No")


#task 3
E = input("Enter residential or commercial")
U = int(input("Enter a unit"))

if E == "residential":
    if U >= 0 and U <= 100:
        print(3 * U)
    elif U >= 101 and U <= 200:
        print(5 * U)
    elif U > 200:
        print(7 * U)
    else:
        print("Invalid Input")

elif E == "commercial":
    if U >= 0 and U <= 100:
        print(5 * U)
    elif U >= 101 and U <= 200:
        print(7 * U)
    elif U > 200:
        print(10 * U)
    else:
        print("Invalid Input")

else:
    print("Invalid Input")


#task 4
distance = int(input("Enter a distance "))
print(distance)

if distance <= 5:
    fare = distance * 10
elif distance <= 15:
    fare = (5 * 10) + (distance - 5) * 8
else:
    fare = (5 * 10) + (10 * 8) + (distance - 15) * 6

if fare < 50:
    fare = 50

print("Total fare: ",fare)


#task 5
a = int(input("Enter a side a "))
print(a)
b = int(input("Enter a side b "))
print(b)
c = int(input("Enter a side c"))
print(c)

if (a + b) <= c or (b +c) <= a or (c + a) <= b:
    print("Not a valid triangle")
else:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


#task 6
n = int(input("Enter a number "))
print(n)

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("number itself")


#task 7
stream = input("Enter your stream (Science/Commerce/Arts): ")
print(stream)
match stream:
    case"science":
        sub = input("Enter sub-choice (Medical/Engineering): ")
        match sub:
            case "Medical":
                print("Chosen Path: Science → Medical")
            case "Engineering":
                print("Chosen Path: Science → Engineering")
            case _:
                print("Invalid sub-choice for Science")

    case "Commerce":
        sub = input("Enter sub-choice (CA/B Com): ")
        match sub:
            case "CA":
                print("Chosen Path: Commerce → CA")
            case "B Com":
                print("Chosen Path: Commerce → B Com")
            case _:
                print("Invalid sub-choice for Commerce")

    case "Arts":
        sub = input("Enter sub-choice (History/Literature): ")
        match sub:
            case "History":
                print("Chosen Path: Arts → History")
            case "Literature":
                print("Chosen Path: Arts → Literature")
            case _:
                print("Invalid sub-choice for Arts")

    
    case _:
        print("Invalid stream entered")


#task 8
time = int(input("Enter show time (in 24-hour format): "))
print(time)

if time >= 9 and time < 12:
    print("Morning Show")
elif time >= 12 and time < 16:
    print("Matinee Show")
elif time >= 16 and time < 20:
    print("Evening Show")
elif time >= 20 and time <= 24:
    print("Night Show")
else:
    print("Invalid input")


#task 9
km = float(input("Enter distance in kilometers: "))
print(km)
choice = int(input("Choose conversion:\n1 → Meters\n2 → Centimeters\n3 → Millimeters\n4 → Miles\nEnter choice: "))
print(choice)

match choice:
    case 1:
        print("Result:", km * 1000, "meters")
    case 2:
        print("Result:", km * 100000, "centimeters")
    case 3:
        print("Result:", km * 1000000, "millimeters")
    case 4:
        print("Result:", km * 0.621371, "miles")
    case _:
        print("Invalid Conversion")


#task 10
payment = input("Enter payment mode (UPI/Card/NetBanking/COD): ")
print(payment)

if payment == "UPI":
    print("You selected UPI payment")
elif payment == "Card":
    print("You selected Debit/Credit Card payment")
elif payment == "NetBanking":
    print("You selected Net Banking")
elif payment == "COD":
    print("You selected Cash on Delivery")
else:
    print("Invalid Payment Mode")

