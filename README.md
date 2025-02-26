# PDT02
Arquitectura Producto de Datos MSc Datos


## Sales Prediction Project

Este proyecto implementa un sistema de predicción de ventas usando datos históricos.

## Estructura del Proyecto

sales_prediction/
├── data/
│ ├── raw/ # Datos originales
│ ├── prep/ # Datos procesados
│ ├── predictions/ # Predicciones generadas
│ └── models/ # Modelos entrenados
├── notebooks/
│ ├── EDA.ipynb
│ └── modeling.ipynb
│ └── analyze_predictions.ipynb
├── src/
│ ├── init.py
│ ├── data_processor.py # Procesamiento de datos
│ └── feature_engineering.py # Ingeniería de features
├── prep.py # Script de preparación
├── train.py # Script de entrenamiento
└── inference.py # Script de predicción


## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Preparación de Datos

```bash
python prep.py
```

### Entrenamiento

```bash
./docker/run.sh train
```

### Inferencia

```bash
./docker/run.sh inference
```

## Estructura de Datos

- `data/raw/`: Datos crudos originales
- `data/prep/`: Datos procesados
- `data/inference/`: Datos para predicción
- `data/predictions/`: Resultados de predicciones

Este script:
- Carga el modelo entrenado
- Genera predicciones para nuevos datos
- Guarda resultados en `data/predictions/`

## Resultados

Las predicciones generadas muestran las siguientes características:
- Media: 0.89 unidades
- Mediana: 1.09 unidades
- Desviación estándar: 0.89 unidades
- Rango: [0.01, 20.00] unidades

La distribución de predicciones muestra un patrón típico de ventas minoristas:
- Mayoría de predicciones entre 0 y 2.5 unidades
- Sesgo positivo (cola larga a la derecha)
- Sin predicciones negativas

## Estructura de Módulos

### data_processor.py
- Clase `DataProcessor`: Maneja la limpieza y procesamiento inicial de datos
- Implementa validaciones y transformaciones básicas

### feature_engineering.py
- Clase `FeatureEngineer`: Crea features para el modelo
- Implementa:
  - Features temporales
  - Features de precio
  - Features de categoría
  - Interacciones y ratios

## Dependencias Principales

- pandas
- numpy
- scikit-learn
- lightgbm
- seaborn
- matplotlib



