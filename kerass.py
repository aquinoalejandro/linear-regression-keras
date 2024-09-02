from keras import Sequential
from keras import layers
from keras import optimizers
from pandass import df, x, y

def entrenar():
    # creo el modelo
    model = Sequential()
    model.add(layers.Dense(1, input_shape=(1,), activation="linear"))

    # compilo el modelo
    optimizador = optimizers.SGD(learning_rate=0.0004)
    model.compile(loss="mse", optimizer=optimizador)

    # y entreno el modelo
    batch_size = len(df)
    historial = model.fit(x, y, epochs=10, batch_size=batch_size)

    return historial

