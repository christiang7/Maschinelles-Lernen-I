#import keras
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import Activation
import tensorflow as tf
# define the model 
################################################
# INSERT YOUR CODE HERE                        #
################################################
#model = Sequential()
#model.add(keras.Input(shape=(16,)))
#model.add(Dense(8))


tf.debugging.set_log_device_placement(True)

# Place tensors on the CPU
with tf.device('/CPU:0'):
  a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Run on the GPU
c = tf.matmul(a, b)
print(c)


#keras.tensorflow_backend._get_available_gpus()

gpus = tf.config.list_physical_devices('GPU')
tf.config.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.set_visible_devices(gpus[0], 'GPU')
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])

    #model = tf.keras.Sequential()
      
    #model.add(keras.Input(shape=(16,)))
    #model.add(Dense(8))
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)

