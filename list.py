# Lists: ordered, mutable, allows duplicate elements
myList = ["banana", "apple", "cherry"]
print(myList)

myList.append("lemon")
print(myList)

for i in myList:
    print(i)

# tricks
myList = [0] * 5
print(myList)

myList2 = [0, 23, 44, 1,]

new_list = myList + myList2
print(new_list)

#

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[::-1]
print(a)
