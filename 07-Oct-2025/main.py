# # task 1
# a = int(input("Enter a number "))
# b = int(input("Enter a number "))
# for i in range(a , b+1, 1):
#     print(i)


# # task 2
# a = int(input("enter a number "))
# b = int(input("enter a number "))
# n = int(input("enter a number "))
# c = 0
# while a <= b:
#     if a % n == 0:
#         c = c + 1
#     a = a +1
# print(c)


# # task 3
# s = int(input("enter how many steps "))
# b = 0
# c =0
# while s >= 5000:
#         a = s // 5000
#         b = 20 * a
#         break
# print("Bonus" ,b, "points")

# while s >= 1000:
#         a = s // 1000
#         c = 5 * a
#         break
# print( c , "points")
# print(b + c , "points")


# task 3
s = int(input("Enter how many steps "))
a = s // 5000 * 20
print(a)

b = s // 1000 * 5
print(b) 
print( a + b , "points")


# task 4
a = 1