# --- STEP 1: USER INPUTS ---
weight_kg = float(input("Enter weight in kg: "))
height_inches = float(input("Enter height in inches: "))

# --- STEP 2: CONVERSION & BMI CALCULATION ---
# Convert height from inches to meters (1 inch = 0.0254 meters)
height_m = height_inches * 0.0254

# Calculate BMI = weight (kg) / [height (m)]^2
bmi = weight_kg / (height_m ** 2)

# Display calculated BMI
print(f"\nYour BMI is: {bmi:.2f}")

# --- STEP 3: CATEGORY DETERMINATION & WEIGHT ADJUSTMENT ---
if bmi < 19:
    print("Status: Underweight")
    
    # Target weight for lower bound of healthy range (BMI = 19)
    target_weight = 19 * (height_m ** 2)
    weight_to_gain = target_weight - weight_kg
    print(f"You need to gain at least {weight_to_gain:.2f} kg to reach a healthy weight.")

elif 19 <= bmi <= 25:
    print("Status: Healthy weight")
    print("Congratulations! You are in a healthy weight range.")

elif 25 < bmi <= 29:
    print("Status: Overweight")
    
    # Target weight for upper bound of healthy range (BMI = 25)
    target_weight = 25 * (height_m ** 2)
    weight_to_lose = weight_kg - target_weight
    print(f"You need to lose at least {weight_to_lose:.2f} kg to reach a healthy weight.")

else: # bmi > 29
    print("Status: Obese")
    
    # Target weight for upper bound of healthy range (BMI = 25)
    target_weight = 25 * (height_m ** 2)
    weight_to_lose = weight_kg - target_weight
    print(f"You need to lose at least {weight_to_lose:.2f} kg to reach a healthy weight.")