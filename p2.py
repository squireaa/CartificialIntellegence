import pandas as pd
import re
df = pd.read_csv('cardata.csv')
df = df.dropna()
global X
global y
X = pd.DataFrame()
y = pd.DataFrame()

def get_numbers(string):
    a = re.findall(r'[0-9]+', string)
    return [float(i) for i in a]
def get_average_for_cell(cell_name, dataset):
    for i, cell in enumerate(df[cell_name]):
        dataset.at[i, cell_name] = sum(get_numbers(cell)) / len(get_numbers(cell))
def get_ptrim(cell_name, dataset):
    for i, cell in enumerate(df[cell_name]):
        if cell[0] == "P":
            dataset.at[i, cell_name] = 1
        else:
            dataset.at[i, cell_name] = 0
def one_hottify(cell_name, dataset):
    one_hot_temp = pd.get_dummies(df[cell_name])
    dataset = pd.concat([dataset, one_hot_temp], axis=1)
def transfer_col(cell_name, dataset):
    for i, cell in enumerate(df[cell_name]):
        dataset.at[i, cell_name] = cell

one_hottify('model', y)
one_hottify('color', y)
one_hottify('model_appraisal', X)
one_hottify('color_appraisal', X)
get_average_for_cell('price', y)
get_average_for_cell('mileage', y)
get_average_for_cell('mileage_appraisal', X)
get_average_for_cell('appraisal_offer', X)
get_ptrim('trim_descrip', y)
get_ptrim('trim_descrip_appraisal', y)
transfer_col('model_year', y)
transfer_col('model_year_appraisal', X)
transfer_col('online_appraisal_flag', X)

X.to_csv("X_data.csv", index=False)
y.to_csv("y_data.csv", index=False)