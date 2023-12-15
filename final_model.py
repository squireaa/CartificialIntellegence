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

X_temp = X
y_temp = y

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = load_model('model_model.h5')


def accuracy_test(rows, k):  # k=0 is 10, k=1 is 5, k=2 is 3
    correct_predictions1 = 0
    correct_predictions2 = 0
    cp_len = 0
    rows = rows
    for i in rows:
        try:
            prediction = X_temp.iloc[i].values.reshape(1, -1)
            prediction = scaler.transform(prediction)
            classes = np.array(y_temp.columns)

            proba = model.predict(prediction)

            sorted_models = np.argsort(proba[0])[:-11:-1]

            real_model = y_temp.iloc[i]
            model_column_name = real_model.index[real_model == 1]

            top_ten_predictions = [str(classes[sorted_models[0]]), str(classes[sorted_models[1]]),
                                   str(classes[sorted_models[2]]), str(
                                       classes[sorted_models[3]]),
                                   str(classes[sorted_models[4]]), str(
                                       classes[sorted_models[5]]),
                                   str(classes[sorted_models[6]]), str(
                                       classes[sorted_models[7]]),
                                   str(classes[sorted_models[8]]), str(classes[sorted_models[9]])]
            top_five_predictions = [str(classes[sorted_models[0]]), str(classes[sorted_models[1]]),
                                    str(classes[sorted_models[2]]), str(
                                        classes[sorted_models[3]]),
                                    str(classes[sorted_models[4]])]
            top_three_predictions = [str(classes[sorted_models[0]]), str(classes[sorted_models[1]]),
                                     str(classes[sorted_models[2]])]

            prediction_models = [top_ten_predictions,
                                 top_five_predictions, top_three_predictions]

            correct_model = str(model_column_name[0])

            if correct_model in prediction_models[k]:
                correct_predictions1 += 1
            if correct_model == str(classes[sorted_models[0]]):
                correct_predictions2 += 1
            cp_len += 1

        except IndexError:
            print("a")
            pass
    accuracy1 = correct_predictions1 / cp_len
    accuracy2 = correct_predictions2 / cp_len
    return [accuracy1, accuracy2]


accuracy_10 = accuracy_test(random.sample(range(130000), 1000), 0)
accuracy_5 = accuracy_test(random.sample(range(130000), 1000), 1)
accuracy_3 = accuracy_test(random.sample(range(130000), 1000), 2)
print("The accuracy for the top ten models is: " + str(accuracy_10[0]))
print("The accuracy for the top five models is: " + str(accuracy_5[0]))
print("The accuracy for the top three models is: " + str(accuracy_3[0]))
print("The accuracy for the top model alone in: " + str(accuracy_10[1]))
