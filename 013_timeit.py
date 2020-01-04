import timeit

print("-".join(str(n) for n in range(100)))
# Now I time how long it takes to do the code above 10000 times
s = ''
time_in_seconds = timeit.timeit('s = "-".join(str(n) for n in range(100))', number=10000)
print("It took {} seconds to create that string 10000 times".format(time_in_seconds))
time_in_seconds = timeit.timeit('s = "-".join([str(n) for n in range(100)])', number=10000)
print("It took {} seconds to create that string via list comprehension 10000 times".format(time_in_seconds))
time_in_seconds = timeit.timeit('s = "-".join(map(str,range(100)))', number=10000)
print("It took {} seconds to create that string via map() 10000 times".format(time_in_seconds))
