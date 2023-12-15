import pandas as pd

X = pd.read_csv('X_data.csv')
y = pd.read_csv('y_data.csv')

appraisal = y['trim_descrip_appraisal']

y.drop(columns='trim_descrip_appraisal')
X = pd.concat([X, appraisal], axis=1)

X.to_csv('Xa_data.csv', index=False)
y.to_csv('yb_data.csv', index=False)
