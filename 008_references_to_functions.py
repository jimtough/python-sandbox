
# define a trivial function
def hello():
    print("Hello!")


# output info about the type of 'hello' (a function) and then execute it
print(type(hello))
print(hello.__name__)
hello()

# now create another reference to this function
ref_to_hello = hello

# output info about the type of 'ref_to_hello' and then execute it
print(type(ref_to_hello))
print(ref_to_hello.__name__)
ref_to_hello()

# now delete the original 'hello' reference
del hello
print("'hello' reference has been deleted")
# if uncommented, this would cause an error
# hello()

# looks like the 'del' command only removed the 'hello' reference - we can still use 'ref_to_hello'
print("'ref_to_hello' should still work")
print(type(ref_to_hello))
print(ref_to_hello.__name__)
ref_to_hello()


# define a function that returns a function reference
def get_greeting_function(name='Jim'):
    def greet_jim():
        print("Hello, Jim.")

    def greet_everyone_else():
        print("Hello, " + name + ".")
    if name == 'Jim':
        return greet_jim
    else:
        return greet_everyone_else


greeting_func_ref_a = get_greeting_function()
greeting_func_ref_b = get_greeting_function('Jim')
greeting_func_ref_c = get_greeting_function('Uncle Bob')

print(greeting_func_ref_a.__name__)
print(greeting_func_ref_b.__name__)
print(greeting_func_ref_c.__name__)
greeting_func_ref_a()
greeting_func_ref_b()
greeting_func_ref_c()


# define a function that takes a function reference as an argument
def call_greeting_function(greeting_function_reference):
    print("About to call greeting function")
    greeting_function_reference()
    print("Done!")


call_greeting_function(greeting_func_ref_a)
call_greeting_function(greeting_func_ref_b)
call_greeting_function(greeting_func_ref_c)
