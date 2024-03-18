# Write a Python function that checks whether a passed string is palindrome or not

def check_string(s):
    if s == s[::-1]:
        print("passed string is palindrome")
    else:
        print("passed string is not palindrome")

str = input("Enter string : ")
check_string(str)