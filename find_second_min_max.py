n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num

max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num

second_min = float('inf')
for num in numbers:
    if num != min_val and num < second_min:
        second_min = num

second_max = float('-inf')
for num in numbers:
    if num != max_val and num > second_max:
        second_max = num

print(f"Second Minimum: {second_min}")
print(f"Second Maximum: {second_max}")