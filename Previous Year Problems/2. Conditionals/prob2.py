def calculate_bill(units):
    # Function to calculate electric bill based on net kWh units consumed.
 
    if units <= 50:
        rate = 2.30
    elif units <= 100:
        rate = 3.00
    elif units <= 500:
        rate = 3.50
    elif units <= 1000:
        rate = 4.00
    elif units <= 2000:
        rate = 4.50
    elif units <= 3000:
        rate = 5.00
    elif units <= 4000:
        rate = 5.50
    else:  # Above 4000
        rate = 6.00
        
    total_bill = units * rate
    return total_bill

# --- INPUT READINGS ---
initial_reading = float(input("Enter initial meter reading: "))
final_reading = float(input("Enter final meter reading: "))

# --- CALCULATE NET UNITS ---
if final_reading >= initial_reading:
    net_units = final_reading - initial_reading
else:
    # Rollover logic when meter resets from 99999 to 00001
    # NOTE: If the meter rolled over to 00000 instead of 00001, 
    # use: net_units = (100000 - initial_reading) + final_reading
    net_units = (99999 - initial_reading) + final_reading

# --- CALL FUNCTION & DISPLAY RESULT ---
bill = calculate_bill(net_units)

print("-" * 41)
print(f"Net Electricity Consumed:\t{net_units:.2f} kWh")
print(f"Total Electric Bill:\t\tTk {bill:.2f}")
print("-" * 41)