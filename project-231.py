import pandas
from pandas import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt('books.csv',error_bad_lines==False)

x = dataset[:,[4,11]].values
y = dataset[:,3].values

model=Sequential()

model.add(Dense(number of neurons,input_dim=8,activation='relu'))
model.add(Dense(number of neurons, activation='relu'))
model.add(Dense(number of neurons, activation='relu'))
model.add(Dense(number of neurons,activation='sigmoid'))
model.summary()