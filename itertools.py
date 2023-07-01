# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a,b)
# print(list(prod))


# from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a,2)
# print(list(perm))


# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations(a,2)
# print(list(comb))


# from itertools import accumulate
# import operator
# a = [1, 2, 5, 3, 4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))


#from itertools import groupby

# def smaller_than_3(x):
#     return x<3

# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))

# from itertools import groupby

# persons = [{'name': 'Tim','age':25}, {'name': 'Dan', 'age':25}, {'name': 'Lisa', 'age':27}, {'name': 'rohan', 'age':20}]

# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))


from itertools import count, cycle, repeat

'''for i in count(10):
    print(i)
    if i == 15:
        break '''

'''a = [1,2,3]
for i in cycle(a):
    print(i)'''

'''a =[1,2,3]
for i in repeat[1,4]:
    print(i)'''

