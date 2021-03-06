# first-try.py
# Needed to get myself off Jupyter Notebook and into a proper IDE  :D
#
# I'm using this Python file to practice what I'm learning in this Udemy course:
# https://www.udemy.com/course/complete-python-bootcamp/
#
# This file isn't meant to have any purpose beyond learning/experimenting with Python features.
#

print('Hello, World!')


# *args represents a variable number of args, and is available as a tuple within the method
# NOTE: The name 'args' is a convention, but you could name it anything. The single * is the important part.
def sum_args_and_return_five_percent(*args):
    return sum(args) * 0.05


# *kwargs represents a variable number of named (keyword) args, and is available as a dictionary within the method
# NOTE: The name 'kwargs' is a convention, but you could name it anything. The double ** is the important part.
def print_fruit_of_choice(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('Your fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('You did not provide your fruit of choice')


fivePercentOfSum = sum_args_and_return_five_percent(40, 60, 100)
print("5 percent of sum is: {}".format(fivePercentOfSum))
print_fruit_of_choice(fruit='banana', vegetable='carrot')


def coding_exercise_19(s):
    output_string = ''
    # proper way to iterate a range of values
    for i in range(0, len(s)):
        c = s[i]
        if i % 2 == 0:
            output_string += c.upper()
        else:
            output_string += c.lower()
        i += 1
    return output_string


print("Result for 'foobar': {}".format(coding_exercise_19('foobar')))
print("Result for 'Walter Jeffery': {}".format(coding_exercise_19('Walter Jeffery')))


def spy_game(int_list):
    """
    :param int_list: list of 0 or more integers
    :return: boolean True if the list of integers contains the integers 0, 0, 7, contiguous or not,
        otherwise returns False
    """
    secret_code = [0, 0, 7]
    for i in int_list:
        if secret_code[0] == i:
            # remove the matched value from head of 'secret_code' array (must specify pop(0) and not just pop())
            secret_code.pop(0)
        # Did we match all values of secret_code yet?
        if len(secret_code) == 0:
            return True
    return False


print(spy_game([6, 3, 1, 7, 4]))
print(spy_game([0, 0, 7]))
print(spy_game([]))
print(spy_game([6, 3, 1, 0, 0, 7, 4, 8, 3, 1, 3, 2]))
print(spy_game([6, 0, 108, 0, 999, 69, 7, 4, 8, 3, 1, 3, 2]))
print(spy_game([6, 0, 108, 0, 999, 69, 171, 4, 8, 3, 1, 3, 2]))


list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8]

# Example of built-in 'map()' function
def square_an_int(i):
    return i ** 2
list_of_squared_ints = list(map(square_an_int, list_of_ints))
print(list_of_squared_ints)

# Example of built-in 'filter()' function
def is_even(i):
    return i % 2 == 0
list_of_even_ints = list(filter(is_even, list_of_ints))
print(list_of_even_ints)

# Implement both of the above with lambda expressions
list_of_squared_ints_b = list(map(lambda i:i**2, list_of_ints))
list_of_even_ints_b = list(filter(lambda i:i%2==0, list_of_ints))
print(list_of_squared_ints_b)
print(list_of_even_ints_b)


# -------------------------------------------------------------------------------------------------
# Playing around with variable scopes
# -------------------------------------------------------------------------------------------------
xxx = 100
yyy = 200

def local_reassignment():
    xxx = 111
    yyy = 222
    print('locally reassigned values | xxx: {} | yyy: {}'.format(xxx, yyy))

local_reassignment()
print(xxx)
print(yyy)

def global_reassignment():
    # explicitly declare that we are locally referencing global variable 'xxx' and not creating a new local 'xxx'
    global xxx
    xxx = 111
    yyy = 222
    print('reassigned value | xxx: {} '.format(xxx))

global_reassignment()
print(xxx)
print(yyy)
# -------------------------------------------------------------------------------------------------
