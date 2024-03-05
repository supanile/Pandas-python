import pandas as pd

df = pd.DataFrame([[66,180],[77,195],[58,150],[80,165],[40,170]],columns=['Height', 'Weight'])

print(df)

df1 = df[['Weight']]
print(df1)