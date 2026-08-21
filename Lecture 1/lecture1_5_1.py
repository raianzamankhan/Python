messy_string = "    ### product_id: ETHANOL_99.4%_pure ###    "
print(messy_string)

clean1 = messy_string.strip(" #")
# Removes all leading/trailing spaces and '#' characters until it hits other text (defaults to whitespace)
print(clean1)
# output: product_id: ETHANOL_99.4%_pure

clean2 = clean1.split(": ")
# Splits string into a list using ": " as delimiter (defaults to whitespace if empty)
# Removes the separator itself; use .partition() to keep it as a 3-tuple
print(clean2)
# output: ['product_id', 'ETHANOL_99.4%_pure']

clean3 = clean2[1]
# Grabs the second item (index 1) from the list, returning it as a string

# Indexing:
# data[N] Extracts item at position N (0-based) for strings/lists/tuples, or key N for dicts
# Output preserves original data type for lists/tuples (str always returns str; fails on int/float)

print(clean3)
# output: ETHANOL_99.4%_pure

clean4 = clean3.split("_")
print(clean4)
# output: ['ETHANOL', '99.4%', 'pure']

chem, purity, _ = clean4
# List unpacking: assigns list items in order to variables ('_' ignores unused values)

print(f"Chemical = {chem} | Purity = {purity}")
# output: Chemical = ETHANOL | Purity = 99.4%