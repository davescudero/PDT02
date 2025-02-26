# Modelo de Predicción

## Descripción General

El sistema utiliza LightGBM, un modelo de gradient boosting optimizado para eficiencia y rendimiento. Este modelo fue elegido por sus características clave:

- Alta eficiencia en entrenamiento
- Manejo natural de características categóricas
- Soporte para datos dispersos
- Capacidad de manejo de grandes volúmenes de datos

## Arquitectura del Modelo

### Hiperparámetros Principales

```python
params = {
    'objective': 'regression',      # Tipo de problema
    'metric': 'rmse',              # Métrica de evaluación
    'boosting_type': 'gbdt',       # Tipo de boosting
    'num_leaves': 31,              # Complejidad del árbol
    'learning_rate': 0.05,         # Tasa de aprendizaje
    'feature_fraction': 0.9        # Submuestreo de características
}
```

### Función Objetivo

La función objetivo que el modelo minimiza es el error cuadrático medio:

$
L = \frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2
$

donde:
- $y_i$ es el valor real (logaritmo de ventas)
- $\hat{y}_i$ es la predicción del modelo
- $N$ es el número total de muestras

## Proceso de Entrenamiento

### 1. Preparación de Datos

Los datos se preparan siguiendo estos pasos:

1. Transformación logarítmica de la variable objetivo:
   $
   y = \log(1 + \text{ventas})
   $

2. Normalización de características:
   $
   z = \frac{x - \mu}{\sigma}
   $

### 2. Validación Cruzada

Se utiliza una validación cruzada temporal con las siguientes características:

- Ventana móvil de 3 meses
- Sin solapamiento entre conjuntos
- Preservación del orden temporal

### 3. Entrenamiento Iterativo

El proceso de gradient boosting sigue estos pasos en cada iteración $t$:

1. Cálculo del gradiente negativo:
   $
   g_i = -\frac{\partial L}{\partial \hat{y}_i}
   $

2. Ajuste del árbol de regresión $h_t(x)$ a los residuos

3. Actualización del modelo:
   $
   F_t(x) = F_{t-1}(x) + \eta \cdot h_t(x)
   $
   donde $\eta$ es la tasa de aprendizaje

## Evaluación del Modelo

### Métricas Principales

1. **RMSE (Root Mean Square Error)**:
   $
   \text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2}
   $

2. **R² Score**:
   $
   R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}
   $

### Análisis de Importancia de Características

La importancia de cada característica se calcula usando:

$
\text{Importancia}_j = \sum_{t=1}^T \text{ganancia}_j^t
$

donde:
- $T$ es el número total de árboles
- $\text{ganancia}_j^t$ es la ganancia de información de la característica j en el árbol t

## Inferencia

### Proceso de Predicción

1. Preprocesamiento de datos nuevos
2. Aplicación del modelo:
   $
   \hat{y} = F_T(x)
   $
3. Transformación inversa:
   $
   \text{ventas} = \exp(\hat{y}) - 1
   $

### Optimizaciones

1. **Poda de Árboles**:
   - Eliminación de nodos poco significativos
   - Reducción del tamaño del modelo

2. **Cuantización**:
   - Reducción de la precisión numérica
   - Mejora en velocidad de inferencia

## Monitoreo y Mantenimiento

### Métricas de Monitoreo

1. **Drift de Datos**:
   $
   D_{KL}(P||Q) = \sum_i P(i) \log\frac{P(i)}{Q(i)}
   $
   donde P es la distribución original y Q la nueva

2. **Error de Predicción en Tiempo Real**:
   $
   \text{MAE}_t = \frac{1}{w}\sum_{i=t-w+1}^t |y_i - \hat{y}_i|
   $
   donde w es el tamaño de la ventana de monitoreo

### Reentrenamiento

El modelo se reentrena cuando:

1. El error supera un umbral: $\text{MAE}_t > \theta$
2. El drift de datos es significativo: $D_{KL} > \delta$

## Limitaciones y Consideraciones

1. **Datos Faltantes**:
   - Imputación mediante medias móviles
   - Flags de valores faltantes

2. **Valores Atípicos**:
   - Detección mediante IQR
   - Winsorización en los percentiles 1 y 99

3. **Latencia**:
   - Tiempo máximo de inferencia: 100ms
   - Batch processing para optimización 