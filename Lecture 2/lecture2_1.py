try:
    age = float(input("Enter your age = "))
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You can vote")
    else:
        print("You can not vote")
except ValueError:
    print("Please enter a valid numerical age.")

# try/except handles errors smoothly without crashing the program:
# - ValueError: Raised when converting an invalid data type (e.g., float("hello"))
# - ZeroDivisionError: Raised when dividing any number by 0 (e.g., 100 / 0)