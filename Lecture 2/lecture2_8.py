# Range Equivalent

count = 1             # 1. Initialize the counter variable to 1
while count <= 5:     # 2. Condition: Keep looping as long as count is 5 or less
    print(count)      # 3. Print the current value of count
    count += 1        # 4. Increment count by 1 (same as count = count + 1)

# List Iteration

fruits = ["Apple", "Kiwi", "Fig"]
index = 0
while index < len(fruits): # len(fruits) calculates the total number of items (3)
    print(fruits[index])   # Accesses item at position 'index' (e.g., fruits[0] is "Apple")
    index += 1             # Adds 1 to index so we move to the next item on the next pass

# String Iteration

word = "code"
index = 0
while index < len(word): # len(word) calculates total character count (4)
    print(word[index])   # Accesses character at position 'index' (e.g., word[0] is 'C')
    index += 1           # Adds 1 to index so we move to the next character

# Enumerate Equivalent (Index + Item)

fruits = ["Apple", "Kiwi", "Fig"]
index = 0
while index < len(fruits):
    print(index, fruits[index])  # Prints both index and item
    index += 1