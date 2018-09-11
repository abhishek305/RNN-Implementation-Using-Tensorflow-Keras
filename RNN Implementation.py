import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,LSTM

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)= mnist.load_data()

x_train = x_train/255.0
x_train = x_test/255.0 


model.add(LSTM(128,input_shape=(x_train.shape[1:]),activation='relu',return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32,actiavtion='relu'))
model.add(Dropout(0.2))

model.add(Dense(10,actiavtion='softmax'))

opt.tf.keras.optimizers.Adam(Lr=1e-3,decay=1e-5)

model.compile(Loss='sparse_categorical_crossentropy',optimizer=opt,metrics=['accuray'])

model.fit(x_train,y_train,epochs=3,validation_data=(x_test,y_test))






























          
               

