# Preguntas Frecuentes (FAQ)

## Generales

### ¿Qué tipo de datos necesito para usar el sistema?
El sistema requiere datos históricos de ventas con las siguientes características mínimas:
- Fecha de venta
- ID del producto
- Cantidad vendida
- Precio de venta
- Categoría del producto (opcional pero recomendado)

### ¿Cuántos datos históricos necesito para obtener buenos resultados?
Se recomienda tener al menos 12 meses de datos históricos para capturar patrones estacionales. Sin embargo, el sistema puede funcionar con un mínimo de 3 meses de datos.

### ¿Qué formato deben tener los datos de entrada?
Los datos deben estar en formato CSV con las siguientes características:
- Separador: coma (,)
- Codificación: UTF-8
- Fechas en formato ISO (YYYY-MM-DD)
- Sin valores faltantes en campos críticos

## Técnicos

### ¿Cómo maneja el sistema los valores faltantes?
El sistema utiliza diferentes estrategias según el tipo de dato:
- Valores numéricos: imputación mediante medias móviles
- Categorías: valor especial "DESCONOCIDO"
- Fechas: no se permiten fechas faltantes

### ¿Qué recursos computacionales requiere el sistema?
Requerimientos mínimos recomendados:
- CPU: 4 cores
- RAM: 8GB
- Almacenamiento: 20GB
- Docker instalado

### ¿El sistema puede ejecutarse en GPU?
Sí, el sistema puede aprovechar GPUs NVIDIA si están disponibles. Para activar el soporte GPU:
1. Asegúrese de tener NVIDIA Docker instalado
2. Use el tag `--gpu` al ejecutar los contenedores

## Rendimiento y Precisión

### ¿Qué métricas de rendimiento utiliza el sistema?
Las principales métricas son:
- RMSE (Root Mean Square Error)
- R² Score
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

### ¿Cada cuánto se debe reentrenar el modelo?
Se recomienda reentrenar el modelo en los siguientes casos:
1. Mensualmente con nuevos datos
2. Cuando el error supera un umbral predefinido
3. Cuando hay cambios significativos en los patrones de venta

### ¿Cómo se manejan los productos nuevos sin histórico?
Para productos nuevos, el sistema:
1. Utiliza información de productos similares
2. Aplica técnicas de cold-start
3. Actualiza predicciones conforme se recolectan datos

## Despliegue y Mantenimiento

### ¿Cómo se despliega en producción?
El sistema puede desplegarse de varias formas:
1. Como contenedores Docker independientes
2. En orquestadores como Kubernetes
3. Como parte de un pipeline de MLOps

### ¿Cómo se monitorea el rendimiento en producción?
Se proporcionan varias herramientas:
1. Dashboard de métricas en tiempo real
2. Alertas configurables
3. Logs detallados de predicciones
4. Monitoreo de drift de datos

### ¿Qué hacer si el rendimiento se degrada?
Pasos recomendados:
1. Verificar la calidad de los datos de entrada
2. Analizar los logs de predicciones
3. Comparar distribuciones de datos
4. Reentrenar el modelo si es necesario

## Personalización

### ¿Se pueden agregar nuevas características al modelo?
Sí, el sistema permite:
1. Agregar features personalizados
2. Modificar la ingeniería de características
3. Ajustar hiperparámetros del modelo

### ¿Se puede integrar con otros sistemas?
El sistema ofrece:
1. API REST para integración
2. Webhooks para notificaciones
3. Exportación de predicciones en varios formatos
4. Integración con sistemas de logging externos

### ¿Cómo se pueden ajustar los hiperparámetros?
El sistema proporciona:
1. Interfaz para optimización manual
2. Optimización automática (AutoML)
3. Configuración vía archivos YAML
4. Experimentos A/B 