import pandas as pd

# Load the dataset
file_path = '/home/ducan/Documents/DataScienceTalent/BANG-B-Dataset/03_Customer_Behavior_Data.csv'
data = pd.read_csv(file_path)

# I want to create a new column 'Picking up and returning the item' which is 1 if the customer picked up and returned the item, and 0 otherwise
data['Picking up and returning the item'] = (data['Picking up item'] == True) & (data['Returning item'] == True)

# Group by 'Item ID' and count the number of times each item was picked up and returned
item_picking_returning_summary = data.groupby('Item ID')['Picking up and returning the item'].size().reset_index()

# Sort the items by 'Picking up and returning the item' in descending order to find the top 5
top_5_items = item_picking_returning_summary.sort_values(by='Picking up and returning the item', ascending=False).head(5)

# Define the output file path
output_file_path = '/home/ducan/Documents/DataScienceTalent/top_5_items_picking_returning.csv'

# Save the result to a CSV file
top_5_items.to_csv(output_file_path, index=False)

# Output the file path for download
print(output_file_path)