# Write a Python function to check whether a number is perfect or not. 

def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Enter Number : "))
print(perfect_number(num))