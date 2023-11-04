
# find largest mumber
# a = 40
# b = 30
# c = 25

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))
# if a>=b and a>=c:
#     print(a, " is a largest num")
# if b>=a and b>=c:
#     print(b," is a largest num")
# else:
#     print(c, "is largest num")

a = 10
b = 40

# a = a + b
# b = a - b
# a = a - b

# print(a)
# print(b)

tem = a
a = b
a = tem

print(a)
print(b)

a = 10
b = 20
c = 30

if a>=b and a>=c:
    print("a is greater than b or c")
elif b>=a and b>=c:
    print("b is greater than a or c")
elif c>=a and c>=b:
    print("c is greater than b or a")
else :
    print("")


