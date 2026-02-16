import pandas as pd
df = pd.read_csv('E:\python programs\data.csv') 
age_over_30 = df[df['Age'] > 30]
print("--- People Older than 30 ---")
print(age_over_30)
filtered_data = df[(df['Salary'] > 50000) & (df['Age'] < 40)]
print("\n--- Salary > 50k and Age < 40 ---")
print(filtered_data)
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\n--- Sorted by Salary (High to Low) ---")
print(sorted_df)