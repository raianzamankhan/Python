import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv(r"C:\Users\zaman\Desktop\ChE 208\Python\Lecture 5\cstr_process_data.csv")  
# Loads the CSV dataset from the specified file path into a pandas DataFrame

# print(df.shape)  # Returns a tuple representing the total number of rows and columns in the DataFrame (rows, columns)

# print(df.dtypes)  # Displays the data type (dtype) of every column in the DataFrame

# print(df.info())  # Displays a concise summary of the DataFrame, including non-null counts and column data types

# print(df.describe())  # Generates descriptive statistics for numerical columns, such as mean, standard deviation, min, max, and percentiles

df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Converts the "Timestamp" column from strings into standardized pandas datetime objects

print(df.dtypes)  # Displays the updated data type (dtype) of every column in the DataFrame

print(df.info())  # Displays the updated DataFrame info to confirm the data type change of the Timestamp column

print(df.describe())  # Generates descriptive statistics for numerical columns, such as mean, standard deviation, min, max, and percentiles

print(f"{'-' * 45} Missing Values {'-' * 45}")
print(df.isna())  # Returns a boolean DataFrame of the same shape, marking True for missing values (NaN) and False for valid entries
print(df.isna().sum())  # Counts and displays the total number of missing values (NaN) for each individual column

print(f"{'-' * 45} Dublicated Values {'-' * 45}")
print(df.duplicated())  # Returns a boolean Series indicating whether each row is a duplicate of any previous row (True if duplicate, False otherwise)
print(df.duplicated().sum())  # Counts and displays the total number of duplicate rows across the entire DataFrame

print(f"{'-' * 45} Line Plots {'-' * 45}")
# Create separate line plots tracking key reactor variables over time
# plt.figure() initializes a new plotting canvas for each variable
# plt.plot() renders the time series data against the parsed Timestamp
# plt.title() labels each figure before plt.show() displays them all
# plt.xlabel() and plt.ylabel() set axis labels with respective units

plt.figure()
plt.plot(df["Timestamp"], df["Reactor_Temperature_K"])
plt.title("Time vs Reactor Temp (K)")
plt.xlabel("Timestamp")
plt.ylabel("Reactor Temperature (K)")

plt.figure()
plt.plot(df["Timestamp"], df["Pressure_kPa"])
plt.title("Time vs Pressure (kPa)")
plt.xlabel("Timestamp")
plt.ylabel("Pressure (kPa)")

plt.figure()
plt.plot(df["Timestamp"], df["Conversion_pct"])
plt.title("Time vs Conversion (pct)")
plt.xlabel("Timestamp")
plt.ylabel("Conversion (%)")

plt.show()

print(f"{'-' * 45} Histrograms {'-' * 45}")
# .hist() bins the continuous numerical data to show value spread and identify outliers

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

print(f"{'-' * 45} Box Plots {'-' * 45}")
# .boxplot() plots the median line, interquartile range (IQR box), whiskers, and flier points

plt.figure()
df.boxplot(column="Reactor_Temperature_K")
plt.title("Reactor Temperature (K)")
plt.ylabel("Reactor Temperature (K)")

plt.figure()
df.boxplot(column="Pressure_kPa")
plt.title("Pressure (kPa)")
plt.ylabel("Pressure (kPa)")

plt.figure()
df.boxplot(column="Flow_Rate_Lpm")
plt.title("Flow Rate (L/min)")
plt.ylabel("Flow Rate (L/min)")

plt.figure()
df.boxplot(column="Feed_Concentration_molL")
plt.title("Feed Concentration (mol/L)")
plt.ylabel("Feed Concentration (mol/L)")

plt.figure()
df.boxplot(column="Conversion_pct")
plt.title("Conversion (%)")
plt.ylabel("Conversion (%)")

plt.show()

#--------------------------------------------------

# STEP 1: Find Q1 (25th percentile) and Q3 (75th percentile)
# A percentile tells you what percentage of the sorted data falls below that specific value.
# Q1 (quantile 0.25 / 25th percentile): The value where exactly 25% of the data points are smaller, and 75% are larger.
# Q3 (quantile 0.75 / 75th percentile): The value where exactly 75% of the data points are smaller, and 25% are larger.
# .quantile() sorts the column behind the scenes and picks the number at that exact percentage mark.
q1 = df["Reactor_Temperature_K"].quantile(0.25)
q3 = df["Reactor_Temperature_K"].quantile(0.75)

# STEP 2: Calculate the IQR (Interquartile Range)
# IQR is the distance/spread between the 75th percentile (Q3) and the 25th percentile (Q1).
# It measures the spread of the middle 50% of your data (ignoring extreme high and low tails).
# Formula: IQR = Q3 - Q1
iqr = q3 - q1

# STEP 3: Define the lower and upper outlier boundaries (fences)
# The IQR rule creates a "buffer zone" around the middle 50% of the data using a 1.5 multiplier.
# 1.5 * IQR represents the maximum acceptable distance beyond the quartiles before a point is deemed an anomaly.
# lower_limit: Any data point smaller than (Q1 - 1.5*IQR) is an abnormally low value (lower outlier).
# upper_limit: Any data point larger than (Q3 + 1.5*IQR) is an abnormally high value (upper outlier).
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

# STEP 4: Filter the DataFrame to isolate the outlier rows
# (df["Reactor_Temperature_K"] < lower_limit) checks for readings below the safe minimum.
# (df["Reactor_Temperature_K"] > upper_limit) checks for readings above the safe maximum.
# The pipe symbol "|" means OR (we want any row that fails either condition).
# Wrapping that condition inside df[...] pulls out only the matching anomalous rows.
iqr_outliers = df[(df["Reactor_Temperature_K"] < lower_limit) | (df["Reactor_Temperature_K"] > upper_limit)]

# STEP 5: Count how many outlier rows were caught
# len() counts the total number of rows stored inside the iqr_outliers DataFrame.
print(f"IQR outlier for Reactor_Temperature_K: {len(iqr_outliers)}")

iqr_indices = set(iqr_outliers.index)

#--------------------------------------------------

# STEP 1: Handle missing values (NaN)
# .dropna() removes missing entries so the mean and standard deviation math doesn't return NaN.
clean_temp = df["Reactor_Temperature_K"].dropna()

# STEP 2: Calculate Z-score for each data point
# stats.zscore() computes: (value - mean) / standard_deviation
# It shows how many standard deviations each point is away from the average.
z_scores = stats.zscore(clean_temp)

# STEP 3: Iterate through scores and count outliers
# Initialize a counter at zero.
# Loop through each score in z_scores; if abs(score) > 3, increment the counter by 1.
z_outlier = 0
z_indices = []
for idx, i in enumerate(z_scores):
    if abs(i) > 3:
        z_outlier += 1
        # clean_temp.index[idx] maps the loop counter (idx: 0, 1, 2...) back to the original DataFrame row label
        z_indices.append(clean_temp.index[idx])

# STEP 4: Output the result
# Print the final count using an f-string.
print(f"Z-score outlier for Reactor_Temperature_K: {z_outlier}")

z_indices = set(z_indices)

#--------------------------------------------------

# Find common indices flagged by both IQR and Z-score methods

both_indices = iqr_indices & z_indices
print(f"Flagged by both for Reactor_Temperature_K: {len(both_indices)}")

# --------------------------------------------------
# 1. Duplicate Handling
# --------------------------------------------------
# Count identical rows before removal
num_duplicates = df.duplicated().sum()

# Drop duplicate rows
df_cleaned = df.drop_duplicates()

# Confirm how many were removed
print(f"No. of duplicates removed: {num_duplicates}")

# --------------------------------------------------
# 2. Missing Value Handling
# --------------------------------------------------
# Count total missing cells remaining in the deduplicated data
num_missing = df_cleaned.isnull().sum().sum()

# Drop rows containing missing values
df_cleaned = df_cleaned.dropna()

# Confirm how many were removed
print(f"No. of missing values removed: {num_missing}")

# ==============================================================================
# Part (e) i: Summary Statistics for Each Process Variable
# ==============================================================================
variables = [
    "Reactor_Temperature_K",
    "Pressure_kPa",
    "Flow_Rate_Lpm",
    "Feed_Concentration_molL",
    "Conversion_pct"
]

for variable in variables:
    mean = df_cleaned[variable].mean()
    median = df_cleaned[variable].median()
    std_dev = df_cleaned[variable].std()

    # FORMULA: Coefficient of Variation (CV) = (Standard Deviation / Mean) * 100
    # Shows the extent of variability relative to the mean as a percentage.
    coeff_of_var = (std_dev / mean) * 100

    print(f"--- Statistics for {variable} ---")
    print(f"Mean: {mean:.4f}")
    print(f"Median: {median:.4f}")
    print(f"Standard Deviation: {std_dev:.4f}")
    print(f"Coefficient of Variation (%): {coeff_of_var:.4f}%\n")

# ==============================================================================
# Part (e) iii: Pearson Correlation Coefficient (Temperature vs Conversion)
# ==============================================================================
# FORMULA: Pearson's r = Cov(X, Y) / (std_X * std_Y)
# Measures the strength and direction of the linear relationship between two variables (-1 to +1).
correlation = df_cleaned["Reactor_Temperature_K"].corr(df_cleaned["Conversion_pct"])

print(f"Pearson Correlation (Reactor Temp vs Conversion): {correlation:.4f}")

"""

df_cleaned.to_csv("cstr_process_data_cleaned.csv", index=False)

"""