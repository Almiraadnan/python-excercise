"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.
"""

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
elif num1 == num2:
    print("Both numbers are equal")

