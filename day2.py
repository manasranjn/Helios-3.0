# Tuple
t1 = (1, 2, 3, 4, 5)
# print(t1)
# print(type(t1))

t2 = tuple([1,2,3,4,5])
# print(t2)
# print(type(t2))

# Set Type
l1 = [1,1,1,2,2,3,3,4,5,9,6,]
# print(l1)
s1 = {1,1,1,2,2,3,3,4,5,9,6}
# print(s1)
s2 = set(l1)
# print(s2)

# Dictionary
d1 = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "state": "NY"
    }
}
# print(d1)
# print(type(d1))
# print(d1['name'])

# None Type
n1 = None
# print(n1)
# print(type(n1))

# Operators
# Arithmetic Operators
x = 10
y = 3
# print("Addition:", x + y)
# print("Subtraction:", x - y)
# print("Multiplication:", x * y)
# print("Division:", x / y)
# print("Floor Division:", x // y)
# print("Modulus:", x % y)
# print("Exponent:", x ** y)

# Assignment Operators
p = 10
p += 5 # p = p + 5
p -= 3 # p = p - 3
p *= 2 # p = p * 2
p /= 4 # p = p / 4
p %= 3 # p = p % 3
p **= 2 # p = p ** 2
p //= 5 # p = p // 5
# print(p)

# Comparison Operators
# a = 5
# b = 10
# print("Equal:", a == b)
# print("Not Equal:", a != b)
# print("Greater than:", a > b)
# print("Less than:", a < b)
# print("Greater than or equal to:", a >= b)
# print("Less than or equal to:", a <= b)

# Logical Operators
# a = True
# b = False
# print("Logical AND:", a and b)
# print("Logical OR:", a or b)
# print("Logical NOT:", not a)

# Membership Operators
a = [1, 2, 3, 4, 5]
# print(3 in a)
# print(6 in a)
# print(3 not in a)
# print(6 not in a)

# Identity Operators
x = 5
y = 10
# print(x is y)
# print(x is not y)

# Conditional Statements
# Simple if statement
# age = 40
# if age >= 18:
#     print("You are an adult.")

# if-else statement
# age = 75
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a kid.")

# elif statement
age = 30
# if age < 13:
#     print("You are a kid.")
# elif age < 20:
#     print("You are a teenager.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior.")


if (age > 0 and age < 13):
    print("You are a kid.")
elif (age >= 13 and age < 20):
    print("You are a teenager.")
elif (age >= 20 and age < 65):
    print("You are an adult.")
else:
    print("You are a senior.")