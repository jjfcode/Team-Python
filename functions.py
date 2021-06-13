def print_name():
    print('John')

def print_favorite_movie():
    print('Mad Max')

def two_plus_two():
    val = 2 + 2
    return val

def add_two(num):
    print(num)
    val = num + 2
    return val

def add_two_arg(num1, num2):
    val = num1 + num2
    return val

def multiply_two(num1, num2):
    val = num1 * num2
    return val

# first function
print_name()
# second function
print_favorite_movie()
# 3rd function
print(two_plus_two())
# 3rd function 2ns aproach
sum = two_plus_two()
print(sum)
# 3rd function with math
print(two_plus_two() * 2)
# 4th function
add_two(5)
print(add_two(5))
# 5 function
print(add_two_arg(5, 10))
# 6 function
print(multiply_two(5, 10))

def hello_student(name):
    val = 'Hello ' + name
    return val

print(hello_student('Ashley'))

def packer(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

packer('hi', 'i', 'love', 'python')

def packer1(*args):
    for val in args:
        print(val)

packer1('hi', 'i', 'love', 'python')

def unpacker():
    return (1, 2, 3)

var1, var2, var3 = unpacker()
print(var1)
print(var2)
print(var3)

def unpacker1():
    return 'hey'

var1, var2, var3 = unpacker1()
print(var1)
print(var2)
print(var3)