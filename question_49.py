# Write a Python function to check whether a number is in a given range

def check_number(n):
    if n in range(1,10):
        print(n, "is in range")
    else:
        print(n, "is not in range")

check_number(10)