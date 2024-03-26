# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

# l = [1.1,2.2564,2.2563]
# l.sort()
# print(l[2])

def find_max_min(numbers):
    if not numbers:
        return None, None  
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

decimal_numbers = [3.14, 2.71, 1.618, 0.577, 2.718]
max_num, min_num = find_max_min(decimal_numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
