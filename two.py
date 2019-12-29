# two.py

import one

print("TOP LEVEL in two.py")

one.func()

# Built-in variable __name__ is only set to '__main__' on script that is entry point
if __name__ == '__main__':
    print('two.py is being run directly!')
else:
    print("two.py has been imported")
