# Make simple calculator
# Input: first number, second number and operation
# Operation: + - / * mod pow div
# mod - remainder of division
# pow - exponentiation
# div - integer division
# If operation is / or div or mod and second number is zero, show string "Division by 0!"
# Numbers are float.

# Sample input:
# 5.0
# 2.0
# *
# Sample output:
# 10.0

# Sample input:
# 3.0
# 0.0
# /
# Sample output:
# Division by 0!

a = float(input())
b = float(input())
z = str(input())

if z == '+':
    print(a + b)
elif z == '-':
    print(a - b)
elif z == '/':
    if b == 0:
        print("Division by 0!")
    else:
        print(a / b)
elif z == '*':
    print(a * b)
elif z == 'mod':
    if b == 0:
        print("Division by 0!")
    else:
        print(a % b)
elif z == 'pow':
    print(a ** b)
elif z == 'div':
    if b == 0:
        print("Division by 0!")
    else:
        print(a // b)
