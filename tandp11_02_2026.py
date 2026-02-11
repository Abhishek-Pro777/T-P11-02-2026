# Arithmetic Operators
a = 15
b = 4
print (a+b) # Addition = 19
print (a-b) # Subtraction = 11
print (a*b) # Multiplication = 60
print (a/b) # Division = 3.75
print (a%b) # Modulus = 3
print (a//b) # Floor Division = 3
print (a**b) # Exponentiation = 50625

# Relational Operators
a = 13
b = 33
print (a>b) # False
print (a<b) # True
print (a==b) # False
print (a!=b) # True
print (a>=b) # False
print (a<=b) # True

# Logical Operators
a = True
b = False
print (a and b) # False
print (a or b) # True
print (not a) # False

# Assignment Operators
a = 10
b = a
print (b) # 10
b += a
print (b) # 20
b -= a
print (b) # 10
b *= a
print (b) # 100
b <<= a
print (b) # 102400

# Programming Practice Questions
# 1. Write a program to store your age in a variable and print
# Answer
age = 24
print(age) 

# 2. Create two variables a = 10 and b = 20. Swap their values without using a third variable.
# Answer
a = 10
b = 20
a, b = b, a
print(a)
print(b)

# 3. Take two numbers from user and print their sum, difference, product and division.
# Answer
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

# 4. Take a number from user and check : Is it even or odd:?
# Answer
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 5. Take three numbers and print the largest number. (No built-in functions allowed like max())
# Answer
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

# 6. Calculate a user's age by taking their birth year as input, then use operators to subtract from the current year.
# Answer
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)
