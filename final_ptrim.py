import pandas as pd
import numpy as np
import random
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import load_model
import keras

X = pd.read_csv('X_data.csv')
y = pd.read_csv('y_data.csv')

y = y[y.columns[5:412]]

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = load_model('ptrim_model.h5')

X_temp = pd.read_csv('X_data.csv')
y_temp = pd.read_csv('y_data.csv')['trim_descrip']

def accuracy_test(rows):
    accurate=0
    for i in rows:
        prediction = model.predict(scaler.transform(X_temp.iloc[i].values.reshape(1, -1)))
        actual = y_temp.iloc[i]
        if prediction > .5 and actual == 1:
            accurate +=1
        elif prediction < .5 and actual == 0:
            accurate +=1
    return accurate / len(rows)


print(str(accuracy_test(random.sample(range(130000), 2000))))
        
