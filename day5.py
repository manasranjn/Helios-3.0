# Functions
# 1.Pre-defined/In-built Functions
# upper(), lower(), count(), keys()

# 2.User-defined Functions
def add():
    a = 10
    b = 20
    print(a+b)

# add() 

def addition():
    a = 10
    b = 100

    total = a+b
    return total

sum = addition()

# print(sum)
# print(addition())
# print(addition())
# print(addition())
# print(addition())

# Parameters
# 1.Without Parameters
# def addition():
#     a = 10
#     b = 100

#     total = a+b
#     return total

# 2.With Parameters
def subtract(a,b):
    return a-b

# print(subtract(100,10))
# print(subtract(300,100))
# print(subtract(1000,3210))

# 3.Default Parameters
def multiply(a=1,b=1):
    print(a)
    print(b)
    return a * b

# print(multiply(10,20))
# print(multiply(100))
print(multiply(b=2, a = 10))