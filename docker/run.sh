#!/bin/bash

# Función para mostrar el uso
show_usage() {
    echo "Uso: $0 [prep|train|inference] [opciones]"
    echo ""
    echo "Comandos:"
    echo "  prep      - Ejecuta el preprocesamiento de datos"
    echo "  train     - Ejecuta el contenedor de entrenamiento"
    echo "  inference - Ejecuta el contenedor de inferencia"
    echo ""
    echo "Opciones para train:"
    echo "  --data-dir DIR      - Directorio de datos (default: data)"
    echo "  --model-dir DIR     - Directorio del modelo (default: models)"
    echo "  --model-name NAME   - Nombre del modelo (default: model.joblib)"
    echo ""
    echo "Opciones para inference:"
    echo "  --data-dir DIR      - Directorio de datos (default: data)"
    echo "  --model-dir DIR     - Directorio del modelo (default: models)"
    echo "  --model-name NAME   - Nombre del modelo (default: model.joblib)"
    echo "  --output-dir DIR    - Directorio de salida (default: data/predictions)"
}

# Verificar comando principal
if [ $# -lt 1 ]; then
    show_usage
    exit 1
fi

COMMAND=$1
shift

# Configurar volúmenes base
DATA_VOLUME="$(pwd)/data:/app/data"
MODELS_VOLUME="$(pwd)/models:/app/models"

# Procesar argumentos adicionales
EXTRA_ARGS=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --data-dir|--model-dir|--model-name|--output-dir)
            EXTRA_ARGS="$EXTRA_ARGS $1 $2"
            shift 2
            ;;
        *)
            echo "Argumento desconocido: $1"
            show_usage
            exit 1
            ;;
    esac
done

case $COMMAND in
    "prep")
        echo "Ejecutando preprocesamiento..."
        docker run --rm \
            -v $DATA_VOLUME \
            ml-price-prep:latest
        ;;
    "train")
        echo "Ejecutando entrenamiento..."
        docker run --rm \
            -v $DATA_VOLUME \
            -v $MODELS_VOLUME \
            ml-price-train:latest $EXTRA_ARGS
        ;;
    "inference")
        echo "Ejecutando inferencia..."
        docker run --rm \
            -v $DATA_VOLUME \
            -v $MODELS_VOLUME \
            ml-price-inference:latest $EXTRA_ARGS
        ;;
    *)
        show_usage
        exit 1
        ;;
esac 