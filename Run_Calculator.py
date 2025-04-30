import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def power(x, y): return x ** y
def sqrt(x): return math.sqrt(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x): return math.log(x)
def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number not defined."
    return math.factorial(int(x))

def calculator():
    print("Advanced Calculator")
    print("Available operations:")
    print("1. Add (x + y)")
    print("2. Subtract (x - y)")
    print("3. Multiply (x * y)")
    print("4. Divide (x / y)")
    print("5. Power (x ^ y)")
    print("6. Square root (√x)")
    print("7. Sine (sin x in degrees)")
    print("8. Cosine (cos x in degrees)")
    print("9. Tangent (tan x in degrees)")
    print("10. Logarithm (log x)")
    print("11. Factorial (x!)")

    choice = input("Enter operation number (1-11): ")

    try:
        if choice in ('1', '2', '3', '4', '5'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            operations = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': divide,
                '5': power
            }
            print("Result:", operations[choice](x, y))

        elif choice in ('6', '7', '8', '9', '10', '11'):
            x = float(input("Enter number: "))
            operations = {
                '6': sqrt,
                '7': sin,
                '8': cos,
                '9': tan,
                '10': log,
                '11': factorial
            }
            print("Result:", operations[choice](x))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print("An error occurred:", e)

# Run the calculator
calculator()
