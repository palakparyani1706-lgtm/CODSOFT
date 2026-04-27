# # Simple Calculator

# # Take input from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Show operation choices
# print("\nChoose an operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# choice = input("Enter choice (1/2/3/4): ")

# # Perform calculation
# if choice == '1':
#     result = num1 + num2
#     print("Result:", result)

# elif choice == '2':
#     result = num1 - num2
#     print("Result:", result)

# elif choice == '3':
#     result = num1 * num2
#     print("Result:", result)

# elif choice == '4':
#     if num2 != 0:
#         result = num1 / num2
#         print("Result:", result)
#     else:
#         print("Error: Division by zero is not allowed.")

# else:
#     print("Invalid choice. Please select a valid operation.")


# Simple Calculator with sentence output

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print(f"The addition of {num1} and {num2} is {result}")

elif choice == '2':
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is {result}")

elif choice == '3':
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice.")