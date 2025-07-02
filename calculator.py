# File: calculator.py
# chaj now
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def modulus(x, y):
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
            print("Invalid input. Please enter numbers only.")
            return

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", modulus(num1, num2))
        elif choice == '5':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
