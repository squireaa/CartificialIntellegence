import pandas as pd
import re
df1 = pd.read_csv('cardata.csv')
global df
df = df1.dropna().reset_index(drop=True)
#df = pd.concat([pd.read_csv('X_data.csv'),df['model_appraisal'],df['color_appraisal']],axis=1)
df = pd.concat([pd.read_csv('y_data.csv'),df['model'],df['color']],axis=1)

def one_hotify(cell_name):
    global df
    one_hot_temp = pd.get_dummies(df[cell_name])
    df = pd.concat([df, one_hot_temp], axis=1)
    df = df.drop(columns=[cell_name])


one_hotify('model')
one_hotify('color')
#one_hotify('model_appraisal')
#one_hotify('color_appraisal')

df.to_csv("yb_data.csv", index=False)
#y.to_csv("y_data.csv", index=False)
