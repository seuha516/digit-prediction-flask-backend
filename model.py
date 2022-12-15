import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = tf.keras.models.load_model('./best-model.h5', custom_objects={'tf': tf})
model._make_predict_function()

global graph
graph = tf.get_default_graph() 

def test_model(image):
    with graph.as_default():
        return model.predict(image)