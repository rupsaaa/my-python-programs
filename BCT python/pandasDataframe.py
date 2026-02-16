import pandas as pd 
data = {
    'Name': ['Alex', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 35, 30, 45],
    'Salary': [45000, 60000, 52000, 80000]
}
df = pd.DataFrame(data)  
print(df.head(3))       
print(df['Age'])        