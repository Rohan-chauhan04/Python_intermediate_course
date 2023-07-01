# Errors and Exceptions
# a = 5 
# print(a)

# x = -5
#assert (x>=0), 'x is not positive' #assertion error

# a = 5 / 0  #zero division errror


#suitable way
# try: 
#     a = 5 / 0
# except Exception as e:
#     print(e)


'''try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print("cleaning up...")'''


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x< 5:
        raise ValueTooSmallError('value is too small',x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)