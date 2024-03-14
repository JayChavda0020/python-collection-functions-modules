# Write a Python script to check if a given key already exists in a dictionary. 

d = {1:2, "j":3, 3:4, 4:5}

# print(1 in d)

def key_present(key):
    if key in d:
        print(key, ", key present in the dictionary")
    else:
        print(key, ", key not present in dictionary")

key_present("j")
key_present(5)