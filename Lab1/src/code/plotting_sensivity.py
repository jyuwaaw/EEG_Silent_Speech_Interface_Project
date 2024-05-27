import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the TSV file, skipping the initial header lines
file_path = 'D:\VSCode\Bioinstrumentation\Lab1\src\data\Data files\\Neurotransmitter-Experiment.tsv'
data = pd.read_csv(file_path, sep='\t', skiprows=9)

# Rename columns for convenience
data.columns = ['Date', 'Time', 'Time_Stamp', 'Time_from_Start', 'BIO1', 'Comments']

# Convert data to appropriate types
data['Time_from_Start'] = pd.to_numeric(data['Time_from_Start'], errors='coerce')
data['BIO1'] = pd.to_numeric(data['BIO1'], errors='coerce')

# Drop rows with missing values
data = data.dropna()

# Define the time ranges for the flat lines (manually identified)
time_ranges = [
    (0, 50),    # First flat line segment
    (70, 100),  # Second flat line segment
    (120, 150), # Third flat line segment
    (180, 210)  # Fourth flat line segment
]

# Combine the segments into a single dataset
combined_segments = pd.DataFrame()

for start, end in time_ranges:
    segment = data[(data['Time_from_Start'] >= start) & (data['Time_from_Start'] <= end)]
    combined_segments = pd.concat([combined_segments, segment])

# Perform linear regression on the combined segments
slope, intercept, r_value, p_value, std_err = linregress(combined_segments['Time_from_Start'], combined_segments['BIO1'])

# Multiply the sensitivity by 1000
sensitivity = slope * 1000

# Plot the data
plt.figure(figsize=(15, 6))
plt.plot(data['Time_from_Start'], data['BIO1'], '-', label='Data', color='blue')

# Plot the overall regression line
plt.plot(combined_segments['Time_from_Start'], intercept + slope * combined_segments['Time_from_Start'], color='red', label=f'Overall Fit: y={sensitivity:.2f}x+{intercept:.2f}')

# Annotate the plot
plt.xlabel('Time from Start (sec)')
plt.ylabel('Current')
plt.title('Current vs. Time from Start with Overall Fit')
plt.legend()
plt.grid(True)
plt.show()

# Print the overall sensitivity
print(f'Overall Sensitivity (Slope * 1000): {sensitivity}')
