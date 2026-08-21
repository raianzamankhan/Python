# 1. \n (Newline) and \t (Tab)
print("Line 1\nLine 2")
print("A\tB")

# 2. sep="" (Removes default space between items)
print("A", "B", "C", sep="")       # Output: ABC
print("A", "B", "C", sep="-")      # Output: A-B-C

# 3. end="" (Stays on the same line)
print("Hello ", end="")
print("World")                     # Output: Hello World

# 4. F-String Alignment (<, ^, >)
x = "Apple"
print(f"|{x:<10}|")                # Left-aligned
print(f"|{x:^10}|")                # Centered
print(f"|{x:>10}|")                # Right-aligned
# Fill empty space with dots instead of spaces
print(f"{x:.<10}")  # Output: Apple.....
print(f"{x:.>10}")  # Output: .....Apple
print(f"{x:-^10}")  # Output: --Apple---

# 5. F-String Numbers (decimals and commas)
num = 1250.756
print(f"{num:.2f}")                # 2 decimal places: 1250.76
print(f"{num:,.2f}")               # Commas + 2 decimals: 1,250.76

# 6. String Repetition (Divider lines)
print("-" * 30)                    # Multiplies "-" by 30 to draw a divider line