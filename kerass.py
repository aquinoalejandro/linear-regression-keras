from keras import Sequential
from keras import layers
from keras import optimizers

def entrenar(x, y):
    # creo el modelo
    model = Sequential()
    model.add(layers.Dense(1, input_shape=(1,), activation="linear"))

    # compilo el modelo
    optimizador = optimizers.SGD(learning_rate=0.00001)

    model.compile(loss="mse", optimizer=optimizador)

    # y entreno el modelo
    batch_size = len(x)
    historial = model.fit(x, y, epochs=100, batch_size=batch_size)

    return model, historial

