"""
Este módulo contiene las clases y funciones para el procesamiento de datos de ventas.

Clases:
    DataProcessor: Clase principal para procesamiento de datos
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from sklearn.preprocessing import StandardScaler
import joblib
from typing import Tuple, Optional

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Clase para procesar datos de ventas y preparar features para el modelo.

    Attributes:
        data_path (Path): Ruta base para los datos
        version (str): Versión del procesamiento
    """

    def __init__(self, data_path: Path):
        """
        Inicializa el procesador de datos.

        Args:
            data_path (Path): Ruta base donde se encuentran los datos
        """
        self.data_path = data_path
        self.processed_path = data_path / "processed"
        self.processed_path.mkdir(exist_ok=True)

    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, Optional[pd.DataFrame]]:
        """Carga los datos desde archivos."""
        try:
            sales = pd.read_csv(self.data_path / "sales_train.csv")
            items = pd.read_csv(self.data_path / "items.csv")
            test = pd.read_csv(
                self.data_path / "test.csv",
                na_values=["null", "nan"]
            )
            return sales, items, test
        except Exception as e:
            logger.error(f"Error cargando datos: {str(e)}")
            raise

    def preprocess_sales(self, sales_df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocesa el DataFrame de ventas.

        Args:
            sales_df (pd.DataFrame): DataFrame de ventas crudo

        Returns:
            pd.DataFrame: DataFrame de ventas procesado
        """
        try:
            logger.info("Preprocesando datos de ventas...")

            # Agregar información temporal
            sales_df["date"] = pd.to_datetime(
                sales_df["date"], format="%d.%m.%Y"
            )  # Corregido el formato
            sales_df["month"] = sales_df["date"].dt.month
            sales_df["year"] = sales_df["date"].dt.year

            # Limpiar valores extremos
            sales_df["item_cnt_day"] = sales_df["item_cnt_day"].clip(0, 20)
            sales_df = sales_df[sales_df["item_price"] > 0]

            # Agregar ventas logarítmicas
            sales_df["item_cnt_log"] = np.log1p(sales_df["item_cnt_day"])

            return sales_df

        except Exception as e:
            logger.error(f"Error en preprocesamiento: {str(e)}")
            raise

    def save_processed_data(self, data: pd.DataFrame, filename: str):
        """
        Guarda datos procesados.

        Args:
            data (pd.DataFrame): Datos a guardar
            filename (str): Nombre del archivo
        """
        try:
            # Guardar datos
            output_path = self.processed_path / filename
            data.to_csv(output_path, index=False)
            logger.info(f"Datos guardados en: {output_path}")

        except Exception as e:
            logger.error(f"Error guardando datos: {str(e)}")
            raise

    def process_all(self):
        """
        Ejecuta el pipeline completo de procesamiento.
        """
        try:
            # 1. Cargar datos
            sales_df, items_df, test_df = self.load_data()

            # 2. Preprocesar ventas
            sales_processed = self.preprocess_sales(sales_df)

            # 3. Guardar datos procesados
            self.save_processed_data(sales_processed, "sales_processed.csv")
            self.save_processed_data(items_df, "items_processed.csv")
            self.save_processed_data(test_df, "test_processed.csv")

            logger.info("✅ Procesamiento completo exitoso!")

        except Exception as e:
            logger.error(f"❌ Error en procesamiento: {str(e)}")
            raise
