# nested for loop or pattern programming

# for i in range (0,5):
#     for j in range (0,5):
#         print("*",end = "")
#     print()


# 11111
# 22222
# 33333
# 44444
# 55555
# for i in range (1,6):
#     for j in range (1,6):
#         print(i,end = "")
#     print()

# 12345
# 12345
# 12345
# 12345
# 12345

# for i in range (1,11):
#     for j in range (1,11):
#         print(j,end = "")
#     print()

# 01 02 03 04 05 
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# count = 1
# for i in range (1,6):
#     for j in range (1,6):
#         if count<10:
#             print("0", end = "")
#         print(count, end = " ")
#         count = count+1
#     print()

# 01 02 03 04 05 
# 02 04 06 08 10 
# 03 06 09 12 15 
# 04 08 12 16 20 
# 05 10 15 20 25

# for i in range (1,6):
#     for j in range (1,6):
#         result= j*i
#         if result<10:
#             print("0", end = "")
#         print(j*i, end = " ")
#     print()

# *****
# *   *
# *   *
# *   *
# *****
# n = 5
# for i in range (n):
#     for j in range(n):
#        if i==0 or i==n-1 or j==0 or j==n-1:
#            print("*", end="")
#        else:
#            print(" ", end="")
#     print()

# n = 5
# for i in range (n):
#     for j in range(n):
#        if i==0 or i==n-1 or j==0 or j==n-1:
#            print("*", end="")
#        else:
#            print(" ", end="")
#     print()
# n = 5
# for i in range (n):
#     for j in range(n):
#        if i==0 or i==n-1 or j==0 or j==n-1:
#            print("*", end="")
#        else:
#            print(" ", end="")
#     print()
# ********
# **    **
# * *  * *
# *  **  *
# *  **  *
# * *  * *
# ** ** **
# n = 5
# for i in range (n):
#      for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#      print()

# n = 5
# for i in range (n):
#     for j in range (n):
#         if i==0:
#             print("*", end = "")
#         else:
#             print(" ", end ="")
#         print()

for i in range (1,9):
    for j in range (1,9):
        if i*j:
            print("", end="")
        else:
            print(" ", end="")
        print()


