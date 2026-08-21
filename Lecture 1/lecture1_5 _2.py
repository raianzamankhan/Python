messy_string = "    ### product_id: ETHANOL_99.4%_pure ###    "
print(messy_string)

clean1 = messy_string.strip(" #")
print(clean1)
# output: product_id: ETHANOL_99.4%_pure

clean2 = clean1[12:25]

# Slicing syntax: data[start:stop] uses 0-based indexing
# Extracts items from 'start' up to (but excluding) 'stop' index
# Indexing: 0 is the first item, -1 is the last item
# Alternative using negative index: clean1[12:-5]
# Slicing shortcuts: [:stop] starts from 0; [start:] slices all the way to the end

print(clean2)
# output: ETHANOL_99.4%

clean3 = clean2.split("_")
print(f"Chemical = {clean3[0]} | Purity = {clean3[1]}")
# output: Chemical = ETHANOL | Purity = 99.4%