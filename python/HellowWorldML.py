import tensorflow as tf
import numpy as np
from tensorflow import keras

#creating a neural network
#1 layer and that 1 layer has 1 neuron
#input shape is just 1 value
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

#code to compile the neural network
model.compile(optimizer='sgd', loss='mean_squared_error');

#providing the data
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float);
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype = float);

#All code above defines the neural network
#Code below is used to train the neural network
#This is where it learns the relationship between the xs and ys [from the model.fit call]
model.fit(xs, ys, epochs=150);

#model.predict is used to have the neural network figure out the Y for a previously unknown X
print(model.predict([10.0]))

