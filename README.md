# Regresión Lineal con Keras y Pandas

Este proyecto es una implementación sencilla de un modelo de regresión lineal utilizando Keras y Pandas. El modelo se entrena para predecir el peso de una persona en función de su altura, utilizando un conjunto de datos almacenado en un archivo CSV. El proyecto incluye la creación, compilación y entrenamiento del modelo, así como la visualización de la pérdida a lo largo de las épocas y la recta de regresión resultante.

## Estructura del Proyecto

- **kerass.py**: Contiene la lógica para crear, compilar y entrenar el modelo de regresión lineal utilizando Keras.
- **datos.py**: Se encarga de la lectura de los datos desde un archivo CSV y su organización en variables `x` e `y` para el entrenamiento del modelo.
- **main.py**: Ejecuta el entrenamiento del modelo y proporciona la visualización de los resultados, como la pérdida por época y la recta de regresión.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Requisitos

- Python 3.7 o superior
- Keras
- Pandas
- Matplotlib

## Instalación

Segui estos pasos para instalar y ejecutar el proyecto en tu entorno local:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/aquinoalejandro/linear-regression-keras.git
   cd linear-regression-keras
   ```

2. **Crea un entorno virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # en windows se usa usa `venv\Scripts\activate`
   ```

3. **Instala las dependencias**:

   Ejecuta el siguiente comando para instalar las dependencias listadas en `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Asegúrate de que el archivo de datos esté en su lugar**:

   Asegúrate de que el archivo `altura_peso.csv` esté en el directorio raíz del proyecto. Este archivo debe contener dos columnas: `Altura` y `Peso`.

5. **Ejecuta el proyecto**:

   Podés ejecutar el proyecto simplemente corriendo el archivo `main.py`:

   ```bash
   python main.py
   ```

   Esto va a entrenar el modelo y va a mostrar los graficos.



