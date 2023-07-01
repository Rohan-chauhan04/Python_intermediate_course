# Strings: ordered, immutable, text representation
# my_string = 'I\'m a programmer'
# char = my_string[-1]  # [:2] --> its prints string after two string
# print(char)

# greeting = "Hello"
# if "e" in greeting:
#     print("Yes")
# else:
#     print("no")

my_string = 'how are you doing. '
my_list = my_string.split(" ")
print(my_list)
new_string = ' '.join(my_list)  # --> important
print(new_string)


# %, .formart(), f-strings
# old method
var = 'Tom'
my_string = "the variable is %s" % var
print(my_string)

# .format method, old method
var = 3.141566
my_string = "the variable is {}".format(var)
print(my_string)

# new method
var = 3.145
var2 = 6
my_string = f'the variable is {var} and {var2}'
print(my_string)
