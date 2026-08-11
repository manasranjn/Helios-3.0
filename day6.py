# List Inbuilt methods
l = [10,20,30,True,"Hello", 10.5, 20.5]
# print(l[2])
# print(l[2:4])
# print(l[2:])
# print(l[:4])
# print(l[:])
# print(l[1:-2])

# Methods
# l.append(40)
# print(l)

# l.insert(2, 50)
# print(l)

# l.remove(20)
# print(l)

# a = l.pop(2)
# print(l)
# print(a)

# l.reverse()
# print(l)

l2 = [10,50,20, 90,30,60]

# l2.sort()
# l2.sort(reverse=True)
# l2.reverse()
# print(l2)

# l.extend([40,50,60])
# print(l)

# l2.clear()
# print(l2)

# l3 = l2
# l3.append(100)

# print(l2)
# print(l3)

# l4 = l2.copy()
# l4.append(100)
# print(l2)
# print(l4)

# print(l.count(10))

nums = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

# print(nums)
nums.sort()
print(nums[0])
print(nums[-1])