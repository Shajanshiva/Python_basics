#option 1 - (in-built) only use in python
a = 5
b = 10
print(a,b)
a,b = b,a
print(a,b)

#option 2 - using temp 
a = 2
b = 3
print(a,b)
temp = a
print(temp)
a = b
print(a)
b = temp
print(a,b)

#option 3 - using addition and subraction
x = 5
y = 10
print(x,y)

x = x + y
print(x,y)

y = x - y
print(x,y)

x = x - y
print(x,y)