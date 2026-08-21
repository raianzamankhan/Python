# ==============================================================================
# FOR LOOP QUICK REFERENCE:
# - A 'for' loop automatically visits every item in a sequence one by one,
#   temporarily assigning each item to a variable so you can work with it inside
#   the indented block.
# - 'for item in collection:' process each element sequentially
# - 'for i in range(n):' repeats code 'n' times, starting at 0 up to n - 1 (e.g., range(3) -> 0, 1, 2)
# - Use 'break' to exit early, 'continue' to skip an iteration, 
#   and 'enumerate()' for index-item pairs
# ==============================================================================

# 1. LIST LOOP
fruits = ["Apple", "Kiwi", "Fig"]

for fruit in fruits:
    print(fruit)  # 'fruit' is assigned one list item at a time


# 2. STRING LOOP
word = "Code"

for letter in word:
    print(letter)  # 'letter' is a string of length 1 for each character


# 3. RANGE LOOP
for i in range(1, 4):
    print(i)  # 'i' is an integer sequence starting at 1 up to 3 (stop parameter 4 is excluded)


# 4. ENUMERATE LOOP
# enumerate() returns two values each pass: (index, item)
for index, fruit in enumerate(fruits):
    print(index, fruit)  # index is int (0, 1, 2), fruit is str ("Apple", "Kiwi", "Fig")