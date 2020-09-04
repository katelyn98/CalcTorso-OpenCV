import tensorflow as tf
import matplotlib.pyplot as plt

print(tf.__version__)

#Loading in the Fashion MNIST data
mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

#printing a training image and training label to see what the values look like
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

#normalizing a list
training_images = training_images / 255.0
test_images = test_images / 255.0

#design the model
#three layers
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

#compile the model with an optimizer and loss function
model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

model.fit(training_images, training_labels, epochs = 5)
