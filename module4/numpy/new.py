import pandas as pd

# Create a DataFrame with some duplicate rows
data = {
    'A': [1, 2, 2, 4, 5, 2],
    'B': [5, 6, 6, 8, 9, 6],
    'C': [10, 11, 11, 13, 14, 11]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


import numpy as np
list_1= [[1, 2, 2, 4, 5, 2],[5, 6, 6, 8, 9, 6],[10, 11, 11, 13, 14, 11]]
c= np.array(list_1)
print(c)

print(c[0,1])