# Write a program to check if a number is even or odd
# number = int(input("Enter a number: "))
# # print(type(number))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
#     # print(number , " is divisible by 2.")
# else:
#     print(f"{number} is an odd number.")

# Loops
# For loop
l1 = [10,20,30,40,50]

# for i in l1:
#     print(i)

s1 = "Python is a programming language"

# for s in s1:
#     print(s)

# for i in range(10):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 100000, 3):
#     print(i)


# WAP to print event numbers from 1 to 100 
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)


# WAP to print event numbers from 1 to 100 without using conditional statements
# for i in range(2,101,2):
#     print(i)


# While loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Nested loop
count = 0
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            print(i,j,k)
            count += 1

print(count)