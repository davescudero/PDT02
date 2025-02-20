"""
Script principal para la preparación de datos.
Este script procesa los datos crudos y los prepara para el entrenamiento.
"""

from pathlib import Path
from src.data_processor import DataProcessor
import logging

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Función principal para ejecutar el procesamiento de datos"""
    try:
        # Configurar rutas
        data_path = Path("data")

        # Inicializar procesador
        processor = DataProcessor(data_path)

        # Ejecutar procesamiento
        processor.process_all()

        logger.info("✅ Preparación de datos completada!")

    except Exception as e:
        logger.error(f"❌ Error en preparación: {str(e)}")
        raise


if __name__ == "__main__":
    main()
