# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(l):

    unique_list = []

    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

l1 = [1,2,2,3,4,5,5,]    
print("Unique elements in l1 are : ")
unique(l1)
