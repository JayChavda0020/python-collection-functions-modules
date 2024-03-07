# Write a Python function to get the largest number, smallest num and sum of all from a list. 

l=[]
num = int(input("Enter the number of elements in the list : "))

for i in range(1, num+1):
    e = int(input("Enter the element : "))
    l.append(e)
max = max(l)
min = min(l)
print("List is : ", l)
print("largest element in list is : ", max)
print("Smallest element in list is : ", min)

# Sum of all list

sum = 0
for i in l:
    sum += i 
print("Sum is : ", sum)