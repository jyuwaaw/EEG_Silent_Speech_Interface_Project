import pandas as pd
import matplotlib.pyplot as plt

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

# Plot the data
plt.figure(figsize=(15, 6))
plt.plot(data['Time_from_Start'], data['BIO1'], label='Current over Time', color='blue')
plt.xlabel('Time (sec)')
plt.ylabel('Current (nA)')
plt.title('Current vs. Time from Start')
plt.legend()
plt.grid(True)
plt.show()
