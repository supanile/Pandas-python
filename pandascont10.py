import pandas as pd

df = pd.DataFrame([[66,180],[77,195],[58,150],[80,165],[40,170]],columns=['Height', 'Weight'])

print(df)

df.loc[5] = ([70,187,'male'])
df.loc[6] = ([40,155,'female'])
print(df)

