#task 1
x = int(input("Enter a number x "))
y = int(input("Enter a number y "))
print(x)
print(y)

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x <0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("Point exits at 0,0")


#task 2
