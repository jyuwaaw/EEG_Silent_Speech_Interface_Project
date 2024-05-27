import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file, skipping the first 5 rows and using the 6th row as the header
file_path = 'D:\VSCode\Bioinstrumentation\Lab1\src\data\Data files\\0520_group2.csv'
data = pd.read_csv(file_path, skiprows=5)

# Rename columns for convenience
data.columns = ['Time_sec', 'Potential_V']

# Convert data to appropriate types
data['Time_sec'] = pd.to_numeric(data['Time_sec'], errors='coerce')
data['Potential_V'] = pd.to_numeric(data['Potential_V'], errors='coerce')

# Drop rows with missing values
data = data.dropna()

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(data['Time_sec'], data['Potential_V'], label='Potential over Time', color='blue')
plt.xlabel('Time (sec)')
plt.ylabel('Potential (V)')
plt.ylim(-0.5, 0.6)
plt.title('Potential vs. Time')
plt.legend()
plt.grid(True)
plt.show()
