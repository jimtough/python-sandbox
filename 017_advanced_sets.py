
s1 = {1, 2, 3}
print(s1)

# make a copy of the set, not just a copy of the reference
s2 = s1.copy()
print("s1: {} | s2: {}".format(s1, s2))
s1.remove(2)
print("After removing 2 from s1 | s1: {} | s2: {}".format(s1, s2))

# find the 'difference' between two sets, meaning 'contents of A minus contents of B'
print("s1.difference(s2): {}".format(s1.difference(s2)))
print("s2.difference(s1): {}".format(s2.difference(s1)))

# remove() raises an exception if the value is not in the set, where discard() will simply do nothing in that case
s3 = {'x', 'y', 'z'}
s3.discard('w')
try:
    s3.remove('w')
except KeyError as ke:
    print("Caught a KeyError when calling set.remove() for value that is not in the set: {}".format(ke.args[0]))

s4 = {1, 2, 3, 4}
s5 = {2, 4, 6, 8}
print("s4: {} | s5: {}".format(s4, s5))
# find the 'intersection' of two sets, meaning 'elements contained in both set A and set B'
print("s4.intersection(s5): {}".format(s4.intersection(s5)))
# get the 'union' of two sets, meaning 'elements contained in either OR both set A and set B'
print("s4.union(s5): {}".format(s4.union(s5)))
