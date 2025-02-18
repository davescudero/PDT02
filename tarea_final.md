# Tarea 03

> En el capítulo 4 aprendiste sobre la importancia de escribir código 
limpio cuando tengas que crear un producto de datos. Cuando estas 
construyendo un proyecto de data science, la idea es comenzar con
un notebook para prototipar rápido, experimentar cosas, cuando estes 
listo puedes extraer el código y ponerlo en un script. Recuerda que es
importante documentar el código siguiendo las prácticas que vimos. 

## Objetivo:

Toma el código de tu tarea anterior y conviertelo en un repositorio, utilizando
las mejores prácticas que revisamos para escribir código limpio.

## Entregables

* Un repositorio público en Github.

Puntos que deberás cubrir:

* Crea la estructura del repositorio (revisa la estructura propuesta en clase).
  * Tu notebook o notebooks, los puedes guardar en un directorio que se llame `notebooks`.
  * Tus datos guardalos una carpeta que se llama `data`. Sigue las recomendaciones de la clase. Recuerda modificar el path de la data en tus notebooks para que puedan correr.
* Vas a convertir tu notebook en un conjunto de scripts que vas a guardar en el root del repo.
  - `prep.py`: La entrada del script son datos `data/raw`. La salida del script son datos `prep`.
  - `train.py`: La entrada del script son datos `data/prep`. La salida del script es un modelo entrenado. Puedes checar el código de este blog [Save and Load Machine Learning Models in Python with scikit-learn](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)
  - `inference.py`: La entrada de este script son datos `data/inference` y el modelo entrenado `model.joblib`. La salida de este modelo son predicciones en batch que se guardan en `data/predictions`.
* Haz un refactor de tu código.
    - crea un directorio `src` y ahi crea módulos (scripts.py) con funciones que luego puedas importar a tu código principal (`prep.py`, `train.py`, `inference.py`) que se encuentra en el root.
    - utiliza Docstrings en los módulos y las funciones. Revisa esta sección del [blog](https://realpython.com/documenting-python-code/#:~:text=Module%20docstrings%20are%20placed%20at,objects%20exported%20by%20the%20module) que mostré en clase. 
    - utiliza Docstrings e Inline comments en las funciones (sigue la propuesta de la clase).
* Optimiza el código redundante en loops y funciones.
    - puedes revisar este blog para llevar tus funciones a un siguiente nivel [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
* Documenta tu repositorio con un README.
  - Agrega un arbol con la estructura de tu repositorio. Checa esta documentación [Tree command in Linux with examples](https://www.geeksforgeeks.org/tree-command-unixlinux/).
* Aplica unos linters a tu código.
  - Aplica el pylint a tu script y trata de obetener una calificación de 10/10.
  - Aplica `black` o `flake8` a tu script y busca no tener ningún error.
  - Hay que estirarse para llegar a la meta =).

## Deadline

- Miércoles 19 de febrero via Canvas, colocas la URL de tu repo.