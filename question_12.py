# Write a Python program to convert a list of characters into a string. 

def convert(s):
    new = ""
    
    for i in s:
        new += i 
    print(new)

s = ['J','a','y',' ','C','h','a','v','d','a']
convert(s)