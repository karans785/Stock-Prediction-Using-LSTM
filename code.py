import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the datasets
training_set = pd.read_csv('Google_Stock_Price_Train.csv')
training_set = training_set.iloc[:,1:2].values

#feature scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
training_set = sc.fit_transform(training_set)

#Getting the inputs and the outputs
X_train = training_set[0:1257]
Y_train = training_set[1:1258] 

#Reshaping
X_train = np.reshape(X_train, (1257,1,1))

#Part 2 - Building the RNN

#import libraries
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import LSTM

#initialising the RNN
regressor = Sequential()

#Adding the input layer and LSTM layer
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

#Add the output layer
regressor.add(Dense(units = 1))

#Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

#Fitting the RNN to the Training Set
regressor.fit(X_train, Y_train, batch_size = 32, epochs = 200)


#Part 3 - Making the predictions and visualising the results

#Getting the real stock price of 2017
test_set = pd.read_csv('Google_Stock_Price_Test.csv')
real_stock_price = test_set.iloc[:,1:2].values

#Getting the predicted stock price of 2017
inputs = real_stock_price
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (20,1,1))
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

#Visualizing the result
plt.plot(real_stock_price, color ='red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price,color = 'blue', label = 'Predicted Stock Price')
plt.title('Stock Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()















