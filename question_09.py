# Write a Python function that takes two lists and returns true if they have at least one common member. 

def common(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
            else:
                False
print(common([1,2,3],[1,4,5]))
