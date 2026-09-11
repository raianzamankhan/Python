import pandas as pd
from scipy import stats

df = pd.read_csv(r"C:\Users\zaman\Desktop\ChE 208\Python\Lecture 5\cstr_process_data.csv")
# Loads the CSV dataset from the specified file path into a pandas DataFrame
df["Timestamp"] = pd.to_datetime(df["Timestamp"]) # Converts the "Timestamp" column from strings into standardized pandas datetime objects

from scipy import stats

# List of process columns specified in question (c)
columns = ["Reactor_Temperature_K", "Pressure_kPa", "Flow_Rate_Lpm", "Conversion_pct"]

# Iterate through each column to run IQR, Z-score, and intersection
for column in columns:
    # -------------------------------------------------------------
    # IQR Method
    # -------------------------------------------------------------
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    
    iqr = q3 - q1
    
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    
    iqr_outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]
    print(f"IQR outlier for {column}: {len(iqr_outliers)}")
    
    # Store IQR outlier indices as a set
    iqr_indices = set(iqr_outliers.index)
    
    # -------------------------------------------------------------
    # Z-Score Method
    # -------------------------------------------------------------
    clean_series = df[column].dropna()
    z_scores = stats.zscore(clean_series)
    
    z_outlier = 0
    z_indices = []
    for idx, i in enumerate(z_scores):
        if abs(i) > 3:
            z_outlier += 1
            # clean_series.index[idx] maps loop counter back to original row label
            z_indices.append(clean_series.index[idx])
            
    print(f"Z-score outlier for {column}: {z_outlier}")
    
    # Convert collected Z-score outlier indices to a set
    z_indices = set(z_indices)
    
    # -------------------------------------------------------------
    # Flagged by Both (Intersection)
    # -------------------------------------------------------------
    both_indices = iqr_indices & z_indices
    print(f"Flagged by both for {column}: {len(both_indices)}")
    print("-" * 50)