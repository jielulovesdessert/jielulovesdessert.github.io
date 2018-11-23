import keras

max_len = 25
num_words = 1000
embedding_size = 32
n_classes = 3
epochs = 10


model = keras.Sequential()
model.add(keras.layers.Embedding(num_words, embedding_size, input_shape=(max_len,)))
model.add(keras.layers.LSTM(embedding_size))
model.add(keras.layers.Dense(3, activation='softmax'))
model.compile('adam', 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(x_train, y_train, epochs=epochs, validation_split=0.2)