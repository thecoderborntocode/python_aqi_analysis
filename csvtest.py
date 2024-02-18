import csv
import pandas as pd
import matplotlib.pyplot as plt
# Specify the data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]
# Specify the path to your CSV file
csv_file_path = 'csvtest.csv'

# Open the CSV file in write mode
# with open(csv_file_path, mode='w', newline='') as file:
#     # Create a CSV writer object
#     writer = csv.writer(file)
#
#     # Write the data to the CSV file
#     writer.writerows(data)
file = pd.read_csv('csvtest.csv')
plt.bar(file['country'],file['AQI LEVEL'])
plt.show()
print(f'Data has been written to {csv_file_path}')
