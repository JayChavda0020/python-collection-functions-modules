# How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

l = [2, 33, 222, 14, 25]

print("Original list is : ", l)

l.pop() # we use pop function to remove last element from list

print("*"*50)

print("List after removing last object is : ", l)

''' list[-1] gives the last element of a list, -1 is the index of the list'''