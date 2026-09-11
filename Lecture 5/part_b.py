import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\zaman\Desktop\ChE 208\Python\Lecture 5\cstr_process_data.csv")
# Loads the CSV dataset from the specified file path into a pandas DataFrame
df["Timestamp"] = pd.to_datetime(df["Timestamp"]) # Converts the "Timestamp" column from strings into standardized pandas datetime objects

# =====================================================================
# (b) i. Time series of reactor temperature, pressure, and conversion
# =====================================================================

plt.figure()
plt.plot(df["Timestamp"], df["Reactor_Temperature_K"])
plt.title("Time vs Reactor Temperature")
plt.xlabel("Timestamp")
plt.ylabel("Reactor Temperature (K)")

plt.figure()
plt.plot(df["Timestamp"], df["Pressure_kPa"])
plt.title("Time vs Pressure")
plt.xlabel("Timestamp")
plt.ylabel("Pressure (kPa)")

plt.figure()
plt.plot(df["Timestamp"], df["Conversion_pct"])
plt.title("Time vs Conversion")
plt.xlabel("Timestamp")
plt.ylabel("Conversion (%)")

# =====================================================================
# (b) ii. Distributions (histograms) of all four numeric process variables
# (Reactor Temp, Pressure, Flow Rate, Feed Concentration)
# =====================================================================

plt.figure()
df["Reactor_Temperature_K"].hist()
plt.title("Distribution of Reactor Temperature")
plt.xlabel("Reactor Temperature (K)")
plt.ylabel("Frequency")

plt.figure()
df["Pressure_kPa"].hist()
plt.title("Distribution of Pressure")
plt.xlabel("Pressure (kPa)")
plt.ylabel("Frequency")

plt.figure()
df["Flow_Rate_Lpm"].hist()
plt.title("Distribution of Flow Rate")
plt.xlabel("Flow Rate (L/min)")
plt.ylabel("Frequency")

plt.figure()
df["Feed_Concentration_molL"].hist()
plt.title("Distribution of Feed Concentration")
plt.xlabel("Feed Concentration (mol/L)")
plt.ylabel("Frequency")

# =====================================================================
# (b) iii. Boxplots of all four numeric process variables
# =====================================================================

plt.figure()
df.boxplot(column="Reactor_Temperature_K")
plt.title("Boxplot of Reactor Temperature")
plt.ylabel("Reactor Temperature (K)")

plt.figure()
df.boxplot(column="Pressure_kPa")
plt.title("Boxplot of Pressure")
plt.ylabel("Pressure (kPa)")

plt.figure()
df.boxplot(column="Flow_Rate_Lpm")
plt.title("Boxplot of Flow Rate")
plt.ylabel("Flow Rate (L/min)")

plt.figure()
df.boxplot(column="Feed_Concentration_molL")
plt.title("Boxplot of Feed Concentration")
plt.ylabel("Feed Concentration (mol/L)")

# =====================================================================
# Render all plots to the screen
# =====================================================================
plt.show()