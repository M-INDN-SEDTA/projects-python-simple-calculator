# File: calculator.py
# Change log: added modulus operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    return x % y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Modulus")
    print("5. Divide")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            return

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = modulus(num1, num2)
        elif choice == '5':
            result = divide(num1, num2)

        print("Result:", result)
    else:
        print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
