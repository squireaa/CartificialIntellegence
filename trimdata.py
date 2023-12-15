import pandas as pd

df = pd.read_csv('betterdata.csv')
df = df.dropna()

dfof0 = df.copy()
dfof1 = df.copy()

dfof0 = df[df['trim_descrip'].isin([0])]
countsof0 = dfof0['trim_descrip_appraisal'].value_counts()
print(countsof0, len(dfof0))

dfof1 = df[df['trim_descrip'].isin([1])]
countsof1 = dfof1['trim_descrip_appraisal'].value_counts()
print(countsof1, len(dfof1))
