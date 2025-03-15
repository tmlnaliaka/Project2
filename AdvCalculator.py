import math

def calculate():
    print("\nWelcome to the Dynamic Calculator! 🎯")
    print("Enter a number, then an operation (+, -, *, /, **, %, sqrt).")
    print("Type '=' to finalize and see the result or 'exit' to quit.\n")

    try:
        # Get the first number
        result = float(input("Enter the first number: "))
        
        while True:
            operation = input("Enter operation (+, -, *, /, **, %, sqrt) or '=' to finalize: ").lower()

            if operation == '=':
                print(f"\nFinal Result: {result}\n")
                break
            elif operation == 'exit':
                print("Goodbye! 👋")
                return
            elif operation == 'sqrt':
                if result < 0:
                    print("Error! Cannot calculate the square root of a negative number.")
                else:
                    result = math.sqrt(result)
                continue
            else:
                try:
                    num = float(input("Enter next number: "))
                    if operation == '+':
                        result += num
                    elif operation == '-':
                        result -= num
                    elif operation == '*':
                        result *= num
                    elif operation == '/':
                        if num == 0:
                            print("Error! Division by zero is not allowed.")
                            continue
                        result /= num
                    elif operation == '**':
                        result **= num
                    elif operation == '%':
                        if num == 0:
                            print("Error! Modulus by zero is not allowed.")
                            continue
                        result %= num
                    else:
                        print("Invalid operation! Please enter a valid one.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

            print(f"Current Result: {result}\n")

    except ValueError:
        print("Invalid input! Please start again with a valid number.")

# Run the calculator
calculate()
