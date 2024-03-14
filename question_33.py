# Write a Python script to concatenate following dictionaries to create a new one. 

d1 = {
    "name" : "Jay",
    "age" : 23
}

d2 = {
    "country" : "India",
    "mobile" : 9054003882
}

# d1.update(d2)
# print(d1)
# print("*"*50)

d3 = d1 | d2
print(d3)