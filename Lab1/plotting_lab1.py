import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file, skipping the metadata rows
file_path = '0520_group2.csv'

# Replace with the actual path to your CSV file
df = pd.read_csv(file_path, skiprows=4)

# Rename the columns for clarity
df.columns = ['Time/sec', 'Potential/V']

# Extract the relevant columns for plotting
time = df['Time/sec']
potential = df['Potential/V']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, potential, marker='o', linestyle='-', color='b', label='Potential vs. Time')

# Add title and labels
plt.title('Open Circuit Potential over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Potential (V)')

# Add a legend
plt.legend()

# Show the plot
plt.show()

