import pandas as pd

df = pd.read_csv(r"C:\Users\zaman\Desktop\ChE 208\Python\Lecture 5\cstr_process_data.csv")
# Loads the CSV dataset from the specified file path into a pandas DataFrame
df["Timestamp"] = pd.to_datetime(df["Timestamp"]) # Converts the "Timestamp" column from strings into standardized pandas datetime objects

print("--- Shape of Dataset ---")  # Prints a decorative header
print(df.shape)  # Reports the dimensions (rows, columns) of the dataset

print("\n--- Data Types ---")  # Prints a decorative header with a newline
print(df.dtypes)  # Displays the data type for every column

print("\n--- Descriptive Statistics ---")  # Prints a decorative header with a newline
print(df.describe())  # Generates statistical summaries (mean, min, max, etc.) for numerical columns

print("\n--- Missing Values ---")  # Prints a decorative header with a newline
print(df.isna().sum())  # Counts and reports the total number of missing values per column

print("\n--- Duplicated Rows ---")  # Prints a decorative header with a newline
print(df.duplicated().sum())  # Counts and reports the total number of exact duplicate rows in the dataset

# Filters for rows where Conversion_pct is physically impossible (less than 0 or greater than 100)
suspicious_rows = df[(df["Conversion_pct"] < 0) | (df["Conversion_pct"] > 100)]

# Displays the specific rows that contain these impossible conversion values
print("\n--- Suspicious Rows in Conversion_pct ---")
print(suspicious_rows[["Timestamp", "Conversion_pct"]])