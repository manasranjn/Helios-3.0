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

# insert a key
d1['phone'] = 1234567890
# print(d1)

# update a key
d1['name'] = "Sumit"
# print(d1)

# delete a key
# del d1['age']
# print(d1)

# for key,value in d1.items():
#     print(key,value)

# print(d1.items())
# print(d1.keys())

# for k in d1.keys():
#     print(k)
#     print(d1[k])

# print(d1.values())

# for i in d1.values():
#     print(i)

d2 = d1.copy()
# print(d2)

# d1.clear()
# print(d2)

# print(d1.pop("address"))
# print(d1.popitem())
# print(d1)

# d1.update({'age': 50})
# print(d1)

print(d1.get("name"))
# print(d1.get("addres")) //None