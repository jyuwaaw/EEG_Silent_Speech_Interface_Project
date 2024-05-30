import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the CSV file, skipping the first 5 rows and using the 6th row as the header
file_path = 'D:\\VSCode\\Bioinstrumentation\\Lab1\\src\\data\\Data files\\0520_group2.csv'
data = pd.read_csv(file_path, skiprows=5)

# Rename columns for convenience
data.columns = ['Time_sec', 'Potential_V']

# Convert data to appropriate types
data['Time_sec'] = pd.to_numeric(data['Time_sec'], errors='coerce')
data['Potential_V'] = pd.to_numeric(data['Potential_V'], errors='coerce')

# Drop rows with missing values
data = data.dropna()

# Define the time ranges for sensitivity calculations
time_ranges = [
    (30, 80),    # First range
    (150, 200),  # Second range
    (240, 290)   # Third range
]

# Combine the segments into a single dataset
combined_segments = pd.DataFrame()

for start, end in time_ranges:
    segment = data[(data['Time_sec'] >= start) & (data['Time_sec'] <= end)]
    combined_segments = pd.concat([combined_segments, segment])

# Perform linear regression on the combined segments
slope, intercept, r_value, p_value, std_err = linregress(combined_segments['Time_sec'], combined_segments['Potential_V'])

# Multiply the sensitivity by 1000
sensitivity = slope * 1000

# Plot the data
plt.figure(figsize=(15, 6))
plt.plot(data['Time_sec'], data['Potential_V'], '-', label='Potential over Time', color='blue')

# Plot the overall regression line
plt.plot(combined_segments['Time_sec'], intercept + slope * combined_segments['Time_sec'], color='red', label=f'Overall Fit: y={sensitivity:.2f}x+{intercept:.2f}')

# Annotate the plot
plt.xlabel('Time (sec)')
plt.ylabel('Potential (V)')
plt.ylim(-0.5, 0.6)
plt.title('Potential vs. Time with Overall Fit')
plt.legend()
plt.grid(True)
plt.show()

# Print the overall sensitivity
print(f'Overall Sensitivity (Slope * 1000): {sensitivity}')
