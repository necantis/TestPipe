import pandas as pd

# Read the Excel file
df = pd.read_excel('Numbers.xlsx')

# Calculate the sum of column A and B
df['A+B'] = df['A'] + df['B']

# Write the result to a CSV file
df.to_csv('Output.csv', index=False)
