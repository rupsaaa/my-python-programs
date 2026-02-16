import pandas as pd
df = pd.read_csv('E:\python programs\data.csv') 

print(df.shape)
print(df.dtypes)
print(df.describe())
print(df['City'].value_counts())