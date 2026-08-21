Items = ["Rice", "Oil", "Sugar", "Milk", "Eggs", "Bread", "Butter"]
Price = [110, 180, 75, 65, 120, 55, 210]
Quantity = [2, 1, 3, 4, 2, 2, 1]

Cost = []         # Initialized as an empty list to store computed costs
Total_Cost = 0   # Initialized to zero to accumulate the running total cost

# --- HEADER ---
print("Items", "Price", "Qty", "Cost", sep="\t")
print("-" * 30)

for i in range(0, 7):
    # 1. Calculate cost for the current item
    c = Price[i] * Quantity[i]
    
    # 2. Append cost to list
    Cost.append(c)
    
    # 3. Add current item's cost to total
    Total_Cost += c
    
    # 4. Print current row aligned under headers
    print(Items[i], Price[i], Quantity[i], Cost[i], sep="\t")

# --- FOOTER ---
print("-" * 30)
print(f"Total Cost:\t\t{Total_Cost:.2f}")

if Total_Cost > 1500:
    Discount = Total_Cost * 0.1
    Subtotal = Total_Cost - Discount
    
    print(f"Discount (10%):\t\t{Discount:.2f}")
    print(f"Subtotal:\t\t{Subtotal:.2f}")
    print("\n--- Premium Customer: Thank You! ---")
elif Total_Cost >= 1000:
    Discount = Total_Cost * 0.1
    Subtotal = Total_Cost - Discount
    
    print(f"Discount (10%):\t\t{Discount:.2f}")
    print(f"Subtotal:\t\t{Subtotal:.2f}")
    print("\n--- Discount applied Successfully ---")
elif Total_Cost > 500:
    Discount = Total_Cost * 0.05
    Subtotal = Total_Cost - Discount
    
    print(f"Discount (5%):\t\t{Discount:.2f}")
    print(f"Subtotal:\t\t{Subtotal:.2f}")
    print("\n--- Discount applied Successfully ---")