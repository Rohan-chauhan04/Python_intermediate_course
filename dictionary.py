# Dictionary: Key-Value pairs , Unordered, Mutable
mydict = {"name": "Rohan", "age": 20, "city": "itahari"}
# print(mydict)

# mydict['email'] = 'rohan@123.com'
# print(mydict)

# mydict['email'] = 'coolrohan@123.com'
# print(mydict)


# mydict.pop('age')
# print(mydict)

# mydict.popitem()
# print(mydict)


# if "name" in mydict:
#     print(mydict["name"])

mydict_2 = dict(name="Max", age=21, hobby="cricket")

mydict.update(mydict_2)
print(mydict)
