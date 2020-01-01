def fibonacci_generator(n):
    """
    Example of a Python generator for a Fibonacci sequence
    :param n: Number of values in the generated sequence
    """
    a = 1
    b = 1
    for _ in range(n):
        # The 'yield' keyword tells Python to return this value and then suspend execution
        # of this generator until the next value is requested
        yield a
        # Interesting syntax for updating two variables within the same command...
        a, b = b, a + b


# Use fibonacci_generator instance in an iterable loop
print("Iterate first 10 Fibonacci numbers in a for loop")
for f in fibonacci_generator(10):
    print(f)

print("Request Fibonacci numbers in an infinite while loop until StopIteration error is raised")
# Create another instance of fibonacci_generator with limit of 10 values and get each value from it manually
my_fg = fibonacci_generator(10)
i = 0
while True:
    i += 1
    try:
        print('Call {} | value: {}'.format(i, next(my_fg)))
    except StopIteration:
        print("Caught 'StopIteration' error on Call #{}".format(i))
        break

# Create an iterator for an iterable type (such as string), so we can iterate manually
s = "Hello, World!"
my_str_iterator = iter(s)
while True:
    try:
        print('char: {}'.format(next(my_str_iterator)))
    except StopIteration:
        print("Caught 'StopIteration' error - we must be at end of string")
        break

# Example of 'generator comprehension', which is similar in syntax to 'list comprehension'
print("example of generator comprehension")
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# note the parentheses
gen_comp = (item for item in some_list if item % 3 == 0)
for item in gen_comp:
    print("item: {}".format(item))
