import io

# This module implements an 'in-memory file-like object'.
# Use this when other code expects a file, but you just want to supply input from a string.
# NOTE: Python 3 module 'io' replaces the old Python 2 module 'StringIO'

# https://docs.python.org/3/library/io.html

# arbitrary string
message = "This is just a normal string."

fake_file = io.StringIO(message)
print(fake_file.read())
