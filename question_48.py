# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):
    factorial = 1

    if n < 0:
        print("factorial does not exist for negative number")
    elif n == 0:
        print("factorial of 0 iis 1")
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        print("factorial of", n, "is ", factorial)

num = int(input("Enter number : "))
factorial(num)