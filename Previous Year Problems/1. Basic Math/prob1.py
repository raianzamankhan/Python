# --- GIVEN DATA ---
x_H2SO4 = 0.50  # Mass fraction of H2SO4 (50 wt%)
x_H2O = 0.50    # Mass fraction of H2O (50 wt%)

rho_H2SO4 = 1.834  # g/cm3
rho_H2O = 0.998    # g/cm3

# --- CALCULATION USING GIVEN FORMULA ---
# rho_mix = sum(x_i * rho_i)
rho_mix = (x_H2SO4 * rho_H2SO4) + (x_H2O * rho_H2O)

# --- DISPLAY RESULT ---
print(f"Density of the mixture: {rho_mix:.3f} g/cm^3")