num = int(input("Enter your number: "))

# Step 1: Check if the number is positive, negative, or zero
if num > 0:
    # Nested check for even/odd on positive numbers
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

elif num < 0:
    # Nested check for even/odd on negative numbers
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")

else:
    # Zero is neither positive nor negative, but it is mathematically even
    print("Zero (Even)")