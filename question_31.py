# How will you create a dictionary using tuples in python? 

fruits = ("apple", "banana", "grapes")
color = ("red", "yellow", "green")

dic = {}

for i in range(len(fruits)):
    dic[fruits[i]] = color[i]

print(dic)