import pandas as pd

# Load the dataset
file_path = '/home/ducan/Documents/DataScienceTalent/BANG-B-Dataset/03_Customer_Behavior_Data.csv'
data = pd.read_csv(file_path)

# Calculate the total time spent looking at and holding each item
data['Total Time (s)'] = data['Looking at item (s)'] + data['Holding the item (s)']

# Group by 'Item ID' and sum the 'Total Time (s)' for each item
item_time_summary = data.groupby('Item ID')['Total Time (s)'].sum().reset_index()

# Sort the items by 'Total Time (s)' in descending order to find the top 5
top_5_items = item_time_summary.sort_values(by='Total Time (s)', ascending=False).head(5)

# Define the output file path
output_file_path = '/home/ducan/Documents/DataScienceTalent/top_5_items_total_time.csv'

# Save the result to a CSV file
top_5_items.to_csv(output_file_path, index=False)

# Output the file path for download
print(output_file_path)
