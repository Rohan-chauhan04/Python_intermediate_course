# Sets: unordered, mutable, no duplicates
# mySet = {1, 2, 4, 5,4}
# mySet = set("Hello")
# mySet = set() empty set

# mySet.add(1)
# mySet.add(2)
# mySet.add(3)

# print(mySet)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)  # odds.intersection(evens) -odds.difference(prime)
print(u)
