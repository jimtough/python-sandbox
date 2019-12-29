# one.py

def func():
    print("func() in one.py")

print("TOP LEVEL in one.py")

# Built-in variable __name__ is only set to '__main__' on script that is entry point
if __name__ == '__main__':
    print('one.py is being run directly!')
else:
    print("one.py has been imported")
