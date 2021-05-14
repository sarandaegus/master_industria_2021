import tensorflow

model = tf.keras.applications.MobilenteV2()

result = model.predict(image)

print(result)
