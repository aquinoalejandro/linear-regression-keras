from kerass import entrenar
import matplotlib.pyplot as plt
from datos import x, y 

def main():
    modelo, historial = entrenar(x, y)

    # imprimo en pantalla los parámetros del modelo (w y b) después del entrenamiento
    print("Parámetros del modelo:")
    print("w:", modelo.layers[0].get_weights()[0])
    print("b:", modelo.layers[0].get_weights()[1])

    # grafico el error cuadrático medio (ECM) vs. el número de épocas
    plt.plot(historial.history['loss'])
    plt.xlabel('Epocas')
    plt.ylabel('Perdida')
    plt.title('Perdida por epoca')
    plt.show()

    # superpongo la recta de regresión resultante sobre los datos originales y visualizo ambas gráficas
    plt.scatter(x, y)
    plt.plot(x, modelo.predict(x), color='red')
    plt.xlabel('Altura')
    plt.ylabel('Peso')
    plt.title('Recta de regresión')
    plt.show()

    #debo aclarar que cambie los datos del ejercicio para que se vea tanto el emc como la recta de regresión
    #tambien tuve que modificar la cantidad de epocas porque a mi compu no le da la potencia.

main()
