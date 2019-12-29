test_output_file_name = "testfile"

# Using a 'bare' except clause to catch any error that occurs. This is discouraged.
# noinspection PyBroadException
def add_and_print_sum(a, b):
    try:
        the_sum = a + b
    except:
        print("Something went HORRIBLY wrong!")
    else:
        print("All good. Sum is {}.".format(the_sum))
    finally:
        print("So done with this...")


def open_file_and_write_test_line(filename, open_mode):
    try:
        f = open(filename, open_mode)
        print("About to write test line to file '{}'".format(filename))
        f.write("This is a test output line")
    except TypeError:
        # TypeError is irrelevant here, so this block should never be called
        print("There was a TypeError")
    except OSError:
        # OSError will be raised if the open() function fails
        print("There was an OSError!")
    finally:
        print("Finally block always executes")


# noinspection PyBroadException
def ask_for_an_integer():
    the_int = None
    while the_int is None:
        try:
            the_int = int(input("Please input an integer value: "))
        except:
            print("OOPS! That is not a valid integer value!")
    print("You entered this integer: [{}]".format(the_int))
    return the_int


add_and_print_sum(10, 10)
add_and_print_sum(10, '10')
open_file_and_write_test_line(test_output_file_name, 'w')
# This will raise an exception because method needs write access
open_file_and_write_test_line(test_output_file_name, 'r')
open_file_and_write_test_line(test_output_file_name, 'a')
ask_for_an_integer()
