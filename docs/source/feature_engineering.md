# Ingeniería de Características

Este módulo contiene las clases y funciones necesarias para transformar los datos procesados en características (features) útiles para el modelo de predicción de ventas.

## Clase FeatureEngineer

La clase principal `FeatureEngineer` se encarga de crear y transformar las características para el modelo.

### Inicialización

```python
engineer = FeatureEngineer(data_path=Path("data"))
```

### Características Generadas

El módulo genera las siguientes características principales:

1. **Características Temporales**:
   - `sales_ema_2m`: Media móvil exponencial de ventas con ventana de 2 meses
   
2. **Características de Precio**:
   - `trend_2m`: Tendencia de precios en ventana de 2 meses
   - `sales_volatility`: Volatilidad de ventas en ventana de 3 meses

3. **Características de Categoría**:
   - `category_avg`: Promedio de ventas por categoría
   
4. **Características Compuestas**:
   - `trend_volatility_ratio`: Ratio entre tendencia y volatilidad
   - `hierarchical_ma_interaction`: Interacción entre promedios de categoría y tendencias

### Flujo de Trabajo

El proceso de generación de características sigue estos pasos:

1. **Carga de Datos**:
   ```python
   sales_df, items_df, test_df = engineer.load_processed_data()
   ```

2. **Creación de Características**:
   ```python
   X, y = engineer.create_all_features()
   ```

3. **Preparación para Test**:
   ```python
   X_test = engineer.create_all_features_for_test(test_df, sales_df, items_df)
   ```

### Almacenamiento

Las características generadas se guardan en los siguientes archivos:

- `data/processed/X_train_scaled.csv`: Características de entrenamiento escaladas
- `data/processed/y_train.csv`: Variable objetivo
- `data/processed/scaler.joblib`: Objeto escalador para normalización

## Uso en Docker

El módulo está integrado en los contenedores Docker y se utiliza automáticamente durante:

1. **Entrenamiento**:
   ```bash
   ./docker/run.sh train
   ```

2. **Inferencia**:
   ```bash
   ./docker/run.sh inference
   ```

## Notas Técnicas

- Las características numéricas se escalan usando `StandardScaler`
- Los valores faltantes se manejan con estrategias específicas para cada característica
- Se implementan técnicas de agregación temporal para capturar patrones históricos 