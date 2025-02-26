# Detalles Matemáticos

Este documento describe en detalle las fórmulas matemáticas y los conceptos utilizados en cada módulo del sistema.

## Preprocesamiento de Datos

### Transformación Logarítmica de Ventas
Para manejar la asimetría en los datos de ventas, aplicamos una transformación logarítmica:

$
y = \log(1 + x)
$

donde:
- $x$ es la cantidad de ventas original (`item_cnt_day`)
- $y$ es la cantidad transformada (`item_cnt_log`)
- Se usa $\log(1 + x)$ en lugar de $\log(x)$ para manejar valores de cero

## Ingeniería de Características

### Características Temporales

#### Media Móvil Exponencial (EMA)
La EMA de ventas se calcula como:

$
\text{EMA}_t = \alpha \cdot x_t + (1-\alpha) \cdot \text{EMA}_{t-1}
$

donde:
- $\text{EMA}_t$ es el valor de la media móvil en el tiempo t
- $x_t$ es el valor actual
- $\alpha = \frac{2}{span + 1}$ es el factor de suavizado
- `span = 2` para nuestra ventana de 2 meses

### Características de Precio

#### Tendencia de Precios
La tendencia de precios se calcula usando una media móvil simple:

$
\text{trend}_{2m} = \frac{1}{n}\sum_{i=t-n+1}^t p_i
$

donde:
- $p_i$ es el precio en el tiempo i
- $n = 2$ para nuestra ventana de 2 meses

#### Volatilidad de Ventas
La volatilidad se calcula como la desviación estándar móvil:

$
\text{volatility} = \sqrt{\frac{1}{n-1}\sum_{i=t-n+1}^t (x_i - \bar{x})^2}
$

donde:
- $x_i$ son las ventas en el tiempo i
- $\bar{x}$ es la media móvil de ventas
- $n = 3$ para nuestra ventana de 3 meses

### Características de Categoría

#### Promedio por Categoría
Para cada categoría c:

$
\text{category\_avg}_c = \frac{1}{|I_c|}\sum_{i \in I_c} x_i
$

donde:
- $I_c$ es el conjunto de items en la categoría c
- $x_i$ son las ventas del item i

### Características Compuestas

#### Ratio Tendencia-Volatilidad
$
\text{ratio} = \frac{\text{trend}_{2m}}{\max(\text{volatility}, 0.001)}
$

El valor mínimo de 0.001 se usa para evitar división por cero.

#### Interacción Jerárquica
$
\text{interaction} = \text{category\_avg} \times \text{sales\_ema}_{2m} \times \text{trend}_{2m}
$

## Normalización de Características

Todas las características numéricas se normalizan usando StandardScaler:

$
z = \frac{x - \mu}{\sigma}
$

donde:
- $x$ es el valor original
- $\mu$ es la media de la característica
- $\sigma$ es la desviación estándar
- $z$ es el valor normalizado

## Modelo de Predicción

### LightGBM
Utilizamos LightGBM, un modelo de gradient boosting que minimiza la función de pérdida:

$
L = \frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2
$

donde:
- $y_i$ es el valor real (logaritmo de ventas)
- $\hat{y}_i$ es la predicción del modelo
- $N$ es el número total de muestras

### Métricas de Evaluación

#### RMSE (Root Mean Square Error)
$
\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2}
$

#### Score del Modelo
El score se calcula como:

$
\text{score} = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}
$

donde $\bar{y}$ es la media de los valores reales. 