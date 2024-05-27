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

# Extract the baseline data (assuming the first few points are the baseline)
baseline_data = data['BIO1'][:10]  # Adjust the range as needed to capture the baseline

# Calculate the standard deviation of the baseline
baseline_std = np.std(baseline_data)

# Perform linear regression on the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(data['Time_from_Start'], data['BIO1'])

# Calculate the LOD
LOD = (3 * baseline_std) / slope

# Plot the data with the regression line
plt.figure(figsize=(15, 6))
plt.plot(data['Time_from_Start'], data['BIO1'], '-', label='Data')
plt.plot(data['Time_from_Start'], intercept + slope * data['Time_from_Start'], 'r', label=f'Fit: y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('Time from Start (sec)')
plt.ylabel('BIO1')
plt.title('BIO1 vs. Time from Start')
plt.legend()
plt.grid(True)
plt.show()

print(f'Baseline Standard Deviation: {baseline_std}')
print(f'Least Squares Slope: {slope}')
print(f'Limit of Detection (LOD): {LOD}')
