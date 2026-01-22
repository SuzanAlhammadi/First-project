num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator")

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)