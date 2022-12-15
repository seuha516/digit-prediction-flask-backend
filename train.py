from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np

(train_input,train_target),(test_input,test_target)=keras.datasets.mnist.load_data()
train_scaled=train_input.reshape(-1,28,28,1)/255.0
test_scaled=test_input.reshape(-1,28,28,1)/255.0
train_scaled,val_scaled,train_target,val_target=train_test_split(train_scaled,train_target,test_size=0.2,random_state=42)

model=keras.Sequential()
model.add(keras.layers.Conv2D(64,kernel_size=3,activation='relu',padding='same',input_shape=(28,28,1)))
model.add(keras.layers.Conv2D(64,kernel_size=3,activation='relu',padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Conv2D(128,kernel_size=3,activation='relu',padding='same'))
model.add(keras.layers.Conv2D(256,kernel_size=3,activation='relu',padding='valid'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(256,activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10,activation='softmax'))
model.summary()

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
checkpoint_cb=keras.callbacks.ModelCheckpoint('best-model.h5')
history=model.fit(train_scaled,train_target,epochs=100,
                  validation_data=(val_scaled,val_target),
                  callbacks=[checkpoint_cb])

model.evaluate(val_scaled,val_target)
model.evaluate(test_scaled,test_target)