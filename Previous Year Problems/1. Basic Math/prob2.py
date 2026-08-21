mass_g = 100.0          # Mass of Nitrogen (N2) in grams
temp_C = 23.0           # Temperature in Celsius
p_gauge_psig = 3.00     # Gauge pressure in psig
p_atm_psia = 14.7       # Atmospheric pressure in psia
R = 0.08206             # Universal gas constant in L*atm/(mol*K)
molar_mass_N2 = 28      # Molar mass of Nitrogen gas (N2) in g/mol

n = mass_g / molar_mass_N2
T = temp_C + 273.15

# --- CALCULATE ABSOLUTE PRESSURE (P) IN ATMOSPHERES ---
# 1. Absolute Pressure in psia = Gauge Pressure + Atmospheric Pressure
P_abs_psia = p_gauge_psig + p_atm_psia

# 2. Convert psia to atm (P = P_abs_psia / 14.7)
P = P_abs_psia / p_atm_psia

# --- SOLVE FOR CONTAINER VOLUME (V) ---
V = (n * R * T) / P

# --- DISPLAY RESULTS ---
print(f"Step 1 - Moles (n):\t\t{n:.4f} mol")
print(f"Step 2 - Temperature (T):\t{T:.2f} K")
print(f"Step 3 - Pressure (P):\t\t{P:.4f} atm")
print("-" * 40)
print(f"Step 4 - Volume (V):\t\t{V:.2f} Liters")