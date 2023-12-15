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

y = y[y.columns[4]]

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train.reshape(-1, 1))
y_test = y_scaler.transform(y_test.reshape(-1, 1))

model = load_model('model_year_model.h5')

X_temp = pd.read_csv('X_data.csv')
y_temp = pd.read_csv('y_data.csv')['model_year']

def accuracy_test(rows, k):
    within = 0
    notwithin = 0
    for i in rows:
        prediction = model.predict(scaler.transform(X_temp.iloc[i].values.reshape(1, -1)))
        prediction_unscaled = y_scaler.inverse_transform(prediction.reshape(-1, 1))[0][0]

        difference = abs(y_temp.iloc[i]-prediction_unscaled)
        if difference < k: # the 2 represents how many cars it can be within before 
            within += 1
        else:
            notwithin += 1

    return within / len(rows)

a = accuracy_test(random.sample(range(130000), 1000), 1)
c = accuracy_test(random.sample(range(130000), 1000), 2)
print("The accuracy of the prediction being within the actual is: " + str(a))
print("The accuracy within p/m 1 model year of the actual is: " + str(c))
