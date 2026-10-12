import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# PUBLIC TRANSPORT DATA ANALYSIS

print(" PUBLIC TRANSPORT DATA ANALYSIS")

# 1. Select Excel File
print("\n1. Select your Excel file...")

root = Tk()
root.withdraw()

file_path = askopenfilename(
    title="Select Public Transport Excel File",
    filetypes=[
        ("Excel Files", "*.xlsx *.xls"),
        ("All Files", "*.*")
    ]
)

if file_path == "":
    print("No file selected.")
    exit()

print("\nExcel File Selected:")
print(file_path)

# 2. Read Excel File
try:
    df = pd.read_excel(file_path)
except Exception as e:
    print("\nError while reading Excel file:")
    print(e)
    exit()

print("\nExcel file loaded successfully!")

# 3. Display Complete Data
print("\n")
print("2. PUBLIC TRANSPORT DATA")

print(df.to_string())

# 4. Number of Records and Columns
print("\n")
print("3. DATASET INFORMATION")

print("Number of Records :", len(df))
print("Number of Columns :", len(df.columns))

print("\nColumn Names:")
for column in df.columns:
    print("-", column)

# 5. Data Types
print("\n")
print("4. DATA TYPES")
print(df.dtypes)

# 6. Missing Values
print("\n")
print("5. MISSING VALUES")
print(df.isnull().sum())

# 7. Duplicate Records
print("\n")
print("6. DUPLICATE RECORDS")

print("Duplicate Records :", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# 8. Basic Statistical Analysis
print("\n")
print("7. STATISTICAL SUMMARY")

print(df.describe(include="all"))

# 9. TRANSPORT MODE ANALYSIS

possible_mode_columns = [
    "Transport Mode",
    "Transport_Mode",
    "Mode",
    "Mode of Transport",
    "TransportMode"
]

mode_column = None

for col in possible_mode_columns:
    if col in df.columns:
        mode_column = col
        break

if mode_column is not None:

    print("\n")
    print("8. TRANSPORT MODE ANALYSIS")
    print("Transport Mode Column :", mode_column)

    mode_count = df[mode_column].value_counts()

    print("\nNumber of users by Transport Mode:")
    print(mode_count)

    # Graph
    plt.figure(figsize=(8, 5))
    mode_count.plot(kind="bar")

    plt.title("Number of Users by Transport Mode")
    plt.xlabel("Transport Mode")
    plt.ylabel("Number of Users")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("\nTransport Mode column not found.")

# 10. AVERAGE ANALYSIS

print("\n")
print("9. AVERAGE ANALYSIS")

numeric_columns = df.select_dtypes(include="number").columns

print("Numeric Columns:")
print(list(numeric_columns))

for col in numeric_columns:
    print(
        "Average", col, "=", round(df[col].mean(), 2)
    )

# 11. TIME PERIOD ANALYSIS

possible_time_columns = [
    "Travel Time",
    "Travel_Time",
    "Time",
    "Time Period",
    "Time_Period",
    "Duration",
    "Journey Time"
]

time_column = None

for col in possible_time_columns:
    if col in df.columns:
        time_column = col
        break

if time_column is not None:

    print("\n")
    print("10. TIME PERIOD ANALYSIS")

    print("Time Column :", time_column)

    print("\nTime Period / Travel Time Counts:")
    print(df[time_column].value_counts())

    plt.figure(figsize=(8, 5))

    df[time_column].value_counts().plot(kind="bar")

    plt.title("Public Transport by Time Period")
    plt.xlabel("Time Period")
    plt.ylabel("Number of Records")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("\nTime Period column not found.")

# 12. NUMERIC COLUMN GRAPHS

print("\n")
print("11. NUMERIC DATA ANALYSIS")

for col in numeric_columns:

    plt.figure(figsize=(8, 5))

    df[col].plot(kind="hist", bins=10)

    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

# 13. CORRELATION

if len(numeric_columns) >= 2:

    print("\n" )
    print("12. CORRELATION ANALYSIS")

    correlation = df[numeric_columns].corr()

    print(correlation)

print("\n")
print("13. FINAL PROJECT SUMMARY")
print("Total Records :", len(df))
print("Total Columns :", len(df.columns))

if mode_column is not None:

    most_used_mode = df[mode_column].value_counts().idxmax()
    highest_count = df[mode_column].value_counts().max()

    print(
        "Most Used Transport Mode :",
        most_used_mode
    )

    print(
        "Number of Users :",
        highest_count
    )

print("\nNumeric Columns Average:")

for col in numeric_columns:
    print(
        col,
        ":",
        round(df[col].mean(), 2)
    )

print("\n")
print(" ANALYSIS COMPLETED SUCCESSFULLY")

