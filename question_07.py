# Write a Python program to remove duplicates from a list.

l = ["python",1,2,2,"java","python"]

final_list = []

for i in l:
    if i not in final_list:
        final_list.append(i)

print(final_list)