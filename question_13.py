# Write a Python program to select an item randomly from a list. 

import random   

l = ['jay','chavda',True,123,False,'python','tops',10.10]

# for i in range(1,11):
#     l.append(i)

item = random.choice(l)

print(l)
print("*"*50)
print("random item : ", item)
