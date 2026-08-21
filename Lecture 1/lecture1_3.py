n = float(input("The number of moles: "))
T = float(input("The temperature in celcius: ")) +273
V = float(input("The volume in litres: "))
R = 0.0821
P=(n*R*T)/V
print(f"The pressure in atm: {P:.7f}")
#Specifies fixed-point notation (f) with exactly 7 decimal places,
#handling rounding and zero-padding automatically.