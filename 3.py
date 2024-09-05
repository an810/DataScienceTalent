import pandas as pd

# Load the dataset
file_path = '/home/ducan/Documents/DataScienceTalent/BANG-B-Dataset/03_Customer_Behavior_Data.csv'
data = pd.read_csv(file_path)

# Define age group categories
def categorize_age(age):
    if 18 <= age <= 30:
        return 'Teenagers'
    elif 31 <= age <= 60:
        return 'Middle-aged'
    elif age > 60:
        return 'Elderly'
    else:
        return 'Others'

# Add a new column for age group
data['Age Group'] = data['Age'].apply(categorize_age)

# Filter data to include only purchases (assuming putting item into bag indicates a purchase)
purchased_items = data[data['Putting item into bag'] == True]

# Group by Age Group and Item ID, then count the number of purchases for each item in each age group
age_group_item_count = purchased_items.groupby(['Age Group', 'Item ID']).size().reset_index(name='Purchase Count')

# Find the most purchased item in each age group
most_purchased_items = age_group_item_count.loc[age_group_item_count.groupby('Age Group')['Purchase Count'].idxmax()]

# Optionally, save the result to a CSV file
output_file_path = '/home/ducan/Documents/DataScienceTalent/most_purchased_items_by_age_group.csv'
most_purchased_items.to_csv(output_file_path, index=False)
