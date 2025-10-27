# #task 1
# def count_overtime(hours):
#     if hours == []:
#         print("Invalid input")
#     else:
#         a = 0
#         for i in range(0,len(hours), 1):
#             if hours[i] > 8:
#                 a = a + 1
#         print(a)
# count_overtime([9, 7, 8, 10, 6, 9])
# count_overtime([8, 8, 9, 10, 7])
# count_overtime([])

# #task 2
def even_day_pages():

    if pages == []:
        print("Invalid input")
    else:
        a = 0
        for i in range(0, len(pages), 1):
            if i != 0 and i % 2 == 0:
                a = a + pages[i]
        print(a)
try:
    even_day_pages([4])
except TypeError as t:
    print("some error appeard", t)

# try:
#     x = 10 / 0
#     print(x)
# except:
#     print("Oops! Something went wrong.")

# try:
#     x = 10 / 0
# except ZeroDivisionError as g:
#     print("Error occurred:", g)
