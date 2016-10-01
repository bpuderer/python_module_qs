# add to list
lst = [0, 1]
# append object to end
lst.append(2)
# extend list by appending elements from iterable
lst.extend([3, 4])
# insert object before index
lst.insert(2, "insert this before element at index 2")
# see careful.py
lst += [5]
print lst


print '---'


# remove from list
lst = [1, 2, 3, 42]
# remove value, ValueError if not present
lst.remove(3)
# remove at index and return, IndexError if empty or out of range
print lst.pop(1)
# if optional index not provided, last item removed/returned
lst.pop()
print lst


print '---'


# clear a list
lst = [1, 2, 3, 4]
print lst
del lst[:]
# lst[:] = [] also ok
print "cleared:", lst


print '---'


# reverse a list in place
# also see slicing.py
lst = [0, 1, 2, 3]
print lst, "reversed in place:",
lst.reverse()
print lst


print '---'


# count.  also see collections.Counter
lst = [1, 2, 3, 3, 1, 1]
print "3 occurs", lst.count(3), "times in", lst

lst = [[1, 2], [1, 2, 3, 1, 1], [4, 5]]
print "1 occurs", sum(x.count(1) for x in lst), "times in", lst


# docs show example of mutating a list using slicing:
# https://docs.python.org/2.7/tutorial/controlflow.html#for-statements
# from Alex Martelli: http://stackoverflow.com/a/1208792
