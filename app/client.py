# In app/cli.py

# Import the functions and the custom error from your calc.py file
from app.calc import sqrt, factorial, ln, power, CalcError

def main():
    """The main function to run the CLI menu."""
    print("--- Scientific Calculator ---")
    print("Available operations: sqrt, factorial, ln, power, quit")

    while True:
        try:
            # Get user input and convert to lowercase
            choice = input("\nEnter operation: ").strip().lower()

            if choice == "quit":
                print("Exiting calculator.")
                break # Exit the loop

            elif choice == "sqrt":
                x = input("Enter a number: ")
                print("Result:", sqrt(x))

            elif choice == "factorial":
                x = input("Enter a non-negative integer: ")
                print("Result:", factorial(x))

            elif choice == "ln":
                x = input("Enter a positive number: ")
                print("Result:", ln(x))

            elif choice == "power":
                x = input("Enter the base (x): ")
                b = input("Enter the exponent (b): ")
                print("Result:", power(x, b))
            
            else:
                print("Unknown operation. Please choose from the list.")

        except CalcError as e:
            # Catch the custom errors from calc.py and print them nicely
            print("Error:", e)
        except Exception:
            # Catch any other unexpected errors
            print("An unexpected error occurred.")

# This makes the script runnable
if __name__ == "__main__":
    main()