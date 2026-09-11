import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv(r"data_files/cstr_process_data.csv")   # df == data frame

df["Timestamp"] = pd.to_datetime(df["Timestamp"])   # converting datetime string to datetime datetime

print(df.shape) # dimension of the entire data

print(df.dtypes)    # what types of data are present in df

print(df.describe())     # descriptive statistics

print("\nMissing Values:")
print(df.isna().sum())   # outputs the number line of which data lines have something missing

print("\nDuplicate Values:")
print(df.duplicated().sum())     # outputs the number line of which data lines have something missing


print("\n")
#------------------------------------- part b ----------------------------------------
print("\n")

# plots
plt.figure()
plt.plot(df["Timestamp"],df["Reactor_Temperature_K"])
plt.title("Time vs Reactor Temp (K)")

plt.figure()
plt.plot(df["Timestamp"], df["Pressure_kPa"])
plt.title("Time vs Pressure (kPa)")

plt.figure()
plt.plot(df["Timestamp"], df["Conversion_pct"])
plt.title("Time vs Converstion (pct)")

plt.show()


# histograms
plt.figure()
df["Reactor_Temperature_K"].hist()
plt.title("Reactor Temperature (K)")
plt.xlabel("Reactor Temperature (K)")
plt.ylabel("Frequency")

plt.figure()
df["Pressure_kPa"].hist()
plt.title("Pressure (kPa)")
plt.xlabel("Pressure (kPa)")
plt.ylabel("Frequency")

plt.figure()
df["Flow_Rate_Lpm"].hist()
plt.title("Flow Rate (L/min)")
plt.xlabel("Flow Rate (L/min)")
plt.ylabel("Frequency")

plt.figure()
df["Feed_Concentration_molL"].hist()
plt.title("Feed Concentration (mol/L)")
plt.xlabel("Feed Concentration (mol/L)")
plt.ylabel("Frequency")

plt.figure()
df["Conversion_pct"].hist()
plt.title("Conversion_pct")
plt.xlabel("Conversion_pct")
plt.ylabel("Frequency")

plt.show()


# box plots
plt.figure()
df.boxplot(column="Reactor_Temperature_K")
plt.title("Boxplot of Reactor Temperature (K)")
plt.show()




print("\n")
#------------------------------------- part c ----------------------------------------
print("\n")


# IQR rule

variables = ["Reactor_Temperature_K", "Pressure_kPa", "Flow_Rate_Lpm", "Feed_Concentration_molL", "Conversion_pct"]

for variable in variables:
    q1 = df[variable].quantile(0.25)
    q3 = df[variable].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5*iqr
    upper_limit = q3 + 1.5*iqr

    iqr_outlier = df[ (df[variable] < lower_limit) | (df[variable] > upper_limit) ]

    print("IQR outlier for "+ variable +": " + str(len(iqr_outlier)))

print("\n")

# z score method

z_score = stats.zscore(df[variable].dropna())

variables = ["Reactor_Temperature_K", "Pressure_kPa", "Flow_Rate_Lpm", "Feed_Concentration_molL", "Conversion_pct"]

for variable in variables:
    z_outlier = df[variable].dropna()[abs(z_score) > 3]
    print("Z_score outlier for " + variable + ": " + str(len(z_outlier)))



print("\n")
#------------------------------------- part d ----------------------------------------
print("\n")


duplicate = df.duplicated().sum()   # how many duplicate values are there
print("No. of duplicates removed: " + str(duplicate))
df_cleaned = df.drop_duplicates()

missing = df_cleaned.isnull().sum().sum()     # how many missing values are there
print("No. of missing removed: " + str(missing))
df_cleaned = df_cleaned.dropna()




print("\n")
#------------------------------------- part d ----------------------------------------
print("\n")


variables = ["Reactor_Temperature_K", "Pressure_kPa", "Flow_Rate_Lpm", "Feed_Concentration_molL", "Conversion_pct"]

for variable in variables:
    mean = df[variable].mean()
    median = df[variable].median()
    standard_dev = df[variable].std()
    coeff_of_var = (standard_dev / mean) * 100
    print("Mean for " + variable + ": " + str(mean))
    print("Median for " + variable + ": " + str(median))
    print("Standard Deviation for " + variable + ": " + str(standard_dev))
    print("Coefficient of Variance for " + variable + ": " + str(coeff_of_var))

    standard_error = standard_dev / (len(df[variable]) ** 0.5)
    confidence_interval = stats. t.interval(0.95, len(df[variable])-1, loc=mean, scale=standard_error)
    print("Standard error for " + variable + ": " + str(standard_error))
    print("95% confidence interval for " + variable + ": " + str(confidence_interval))

    print()



correlation = df["Reactor_Temperature_K"].corr(df["Conversion_pct"])
print("Pearson Correlation Coeff. of Reactor temp (K) vs Conversion (pct) : " + str(correlation))
