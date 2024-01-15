from keras.models import Sequential
from keras.layers import Dense

import pandas as pd
import os


def create_model():
    path = os.path.join(os.path.expanduser('~/data'), 'data_results.txt')
    x_train = pd.read_csv(path)
    y_train = x_train['labels']

    x_train = pd.read_csv(x_train)
    y_train = pd.read_csv(y_train)

    model = Sequential()
    model.add(Dense(800, input_dim=784, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(x_train, y_train,
              batch_size=200,
              epochs=50,
              verbose=1)


    model.save('model.h5')

    return model
    

create_model()