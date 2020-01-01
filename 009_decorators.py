
def my_decorator(original_func_ref):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func_ref()
        print("Some extra code, after the original function")
    return wrap_func


def func_that_needs_decoration():
    print("I am 'func_that_needs_decoration'!")


# Using the @ decorator syntax gives the same result as this line below:
#    manually_decorated_func_ref = my_decorator(func_that_needs_decoration)
@my_decorator
def func_that_is_decorated():
    print("I am 'func_that_is_decorated'!")


print("Call 'func_that_needs_decoration' directly")
func_that_needs_decoration()
manually_decorated_func_ref = my_decorator(func_that_needs_decoration)
print("Call 'manually_decorated_func_ref'")
manually_decorated_func_ref()
print("Call 'func_that_is_decorated'")
func_that_is_decorated()
