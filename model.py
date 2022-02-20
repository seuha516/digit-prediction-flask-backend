from tensorflow import keras
model=keras.models.load_model('best-model.h5')
def pred(input):
    return model.predict(input.reshape(1,28,28,1)[0:1])
