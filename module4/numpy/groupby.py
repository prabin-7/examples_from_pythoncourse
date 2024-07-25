#you need to perform aggregation or iterate through group to print the data from the group
import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 10, 30, 50, 40]
}

df = pd.DataFrame(data)

# Group by 'Category'
grouped = df.groupby(by='Category', axis=0, as_index=True, sort=True)

for name,group in grouped:
    print(f"the group name is{name}")
    print(group)
# Calculate the sum of 'Values' for each group
grouped_sum = grouped.sum()

print(grouped_sum)
