# # task 1
# def vowel_word(words):
#     a = []
#     b = ["a","e","i","o","u"]
#     if len(words) == 0:
#         print("invalid input")
#     else:
#         for i in words:
#             if i in b:
#                 a.append(i)
#         print(a)
# vowel_word("education")


# # task 2
# def maximum_vowel(words):
#     a =[]
#     if len(words) == 0:
#         print("invalid input")
#     else:
#         for i in 

# a = [45,30,48,19,4]
# b = 47
# for i in range(0,len(a), 1):
#     if a[i] > b:
#         print(i + 1)

a = "Learn python code"
b = "-"
res = ""
for i in a:
    if i == " ":
        res = res + b
    else:
        res += i
print(res)