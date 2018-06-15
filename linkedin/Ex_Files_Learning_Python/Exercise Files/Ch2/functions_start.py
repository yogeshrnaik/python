#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a func1")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result


print("***** func1 *****")
func1()
print(func1())
print(func1)

print("***** func2 *****")
func2(10, 20)
print(func2(10,20))

print("***** cube *****")
print(cube(3))

print("***** power *****")
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))


print("***** multi_add *****")
print(multi_add(1,2,3,4,5))