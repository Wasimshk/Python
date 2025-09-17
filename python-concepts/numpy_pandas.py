"""
NumPy
Purpose: Core library for numerical computing in Python.
Data Type: Works with N-dimensional arrays (ndarray) → homogeneous data (all elements of the same type, usually numbers).
Best For:
Mathematical operations
Linear algebra, statistics
Element-wise array calculations
Performance: Very fast because it’s implemented in C under the hood.
Example:"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())   # 3.0

"""
Pandas
Purpose: Built on top of NumPy, designed for data manipulation and analysis.
Data Type: Works with Series (1D) and DataFrame (2D) → can hold heterogeneous data (numbers, strings, dates, etc.).
Best For:
Working with tabular / labeled data
Data cleaning, filtering, grouping, merging
Handling missing values
Performance: Uses NumPy internally for fast computations but adds labels and indexing.
Example:
"""

import pandas as pd
data = {"Name": ["Ali", "Sara", "John"], "Age": [25, 30, 28]}
df = pd.DataFrame(data)
print(df["Age"].mean())   # 27.666...

# Reading a CSV file into a DataFrame
dataframe = pd.read_csv("candidates.csv")
print(dataframe.head())  # show first 5 rows
print(dataframe.tail())  # show last 5 rows
print(dataframe.columns)  # show column names

# Basic statistics
print(dataframe.describe())  # summary statistics for numerical columns
print(dataframe.info())  # info about DataFrame including non-null counts and data types    
