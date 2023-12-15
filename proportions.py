import pandas as pd

df = pd.read_csv('cardata.csv')
df = df.dropna()

name_counts = df['model'].value_counts()
print(name_counts[:10])
print(len(df))
print((name_counts[0]/len(df)))
print((name_counts[:3].sum()/len(df)))
print((name_counts[:5].sum()/len(df)))
print((name_counts[:10].sum()/len(df)))

name_counts = df['color'].value_counts()
print(name_counts[:10])
print(len(df))
print((name_counts[0]/len(df)))
print((name_counts[:3].sum()/len(df)))
print((name_counts[:5].sum()/len(df)))
'''
name_counts = df['trim_descrip'].value_counts()
print((name_counts[0]/len(df)))

name_counts = df['mileage'].value_counts()
print(len(name_counts))
'''