#Head

import pandas as pd

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6,
9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}

df = pd.DataFrame(data=d)

print("Original DataFrame")

print(df)

print("\nFirst 3 rows of the said DataFrame':")

df1 = df.head(3)

print(df1)