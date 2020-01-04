import pdb

x = [1, 2, 3]
y = 2
z = 3

result = y + z
print(result)
# This appears to be like setting a breakpoint.
# When we hit this line, a (Pdb) prompt will appear in the console.
# HINT: Enter 'q' at the (Pdb) prompt to quit the debug session.
pdb.set_trace()
result2 = y + x
print(result2)

# NOTE: This 'pdb' feature seems totally inferior to the debug support provided in PyCharm!
