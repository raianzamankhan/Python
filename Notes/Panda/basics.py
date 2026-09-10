import pandas as pd

# Convert a dictionary into a DataFrame: keys become column headers, list values become column data

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}

df = pd.DataFrame(data)
print(df)

# Loading a DataFrame

'''

df = pd.read_csv('data.csv')        # Load from CSV
df = pd.read_excel('data.xlsx')     # Load from Excel
df = pd.DataFrame(data_dict)        # Load from dictionary

'''