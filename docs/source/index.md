# Documentación del Proyecto de Predicción de Precios

Bienvenido a la documentación del proyecto de predicción de precios. Este proyecto implementa un sistema de predicción de precios utilizando técnicas de aprendizaje automático y está diseñado para ser fácilmente desplegable usando contenedores Docker.

## Contenido

```{toctree}
:maxdepth: 2
:caption: Guías

working_backwards
architecture
feature_engineering
model
mathematical_details
docker_guide
faq
```

## Características Principales

- **Arquitectura Modular**: Sistema diseñado con componentes independientes y reutilizables
- **Contenedores Docker**: Facilita el despliegue y la reproducibilidad
- **Procesamiento de Datos**: Pipeline robusto para la preparación de datos
- **Ingeniería de Características**: Generación automática de features relevantes
- **Modelo Avanzado**: LightGBM optimizado para predicción de ventas
- **Base Matemática Sólida**: Implementación fundamentada en conceptos estadísticos y matemáticos

## Inicio Rápido

Para comenzar a usar el sistema:

1. **Preparación de Datos**:
   ```bash
   ./docker/run.sh prep
   ```

2. **Entrenamiento del Modelo**:
   ```bash
   ./docker/run.sh train
   ```

3. **Inferencia**:
   ```bash
   ./docker/run.sh inference
   ```

## Estructura del Proyecto

```
proyecto/
├── data/           # Datos de entrada y salida
├── docker/         # Archivos Docker
├── models/         # Modelos entrenados
├── src/           # Código fuente
└── docs/          # Documentación
```

## Fundamentos Matemáticos

El sistema se basa en sólidos principios matemáticos y estadísticos:

- **Preprocesamiento**: Transformaciones logarítmicas y normalización
- **Features**: Medias móviles exponenciales, volatilidad y tendencias
- **Modelo**: Gradient boosting con optimización de pérdida cuadrática
- **Evaluación**: Métricas RMSE y R² para validación

Para más detalles, consulta las secciones de [Detalles Matemáticos](mathematical_details.md) y [Modelo](model.md).

## Contribuir

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear una rama para tu feature
3. Commit de tus cambios
4. Push a la rama
5. Crear un Pull Request

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. 