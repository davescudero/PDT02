"""
Script principal para realizar predicciones con el modelo entrenado.
"""

from pathlib import Path
import sys
import logging
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional

# Agregar el directorio raíz al path
PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

from src.feature_engineering import FeatureEngineer
from src.data_processor import DataProcessor

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def load_model(model_path: Path) -> Optional[object]:
    """Carga el modelo entrenado."""
    try:
        return joblib.load(model_path / "model.joblib")
    except Exception as e:
        logger.error(f"Error cargando modelo: {str(e)}")
        return None


def load_model_and_scaler():
    """
    Carga el modelo entrenado y el scaler.

    Returns:
        tuple: (model, scaler)
    """
    try:
        model = joblib.load(PROJECT_ROOT / "models" / "model.joblib")
        scaler = joblib.load(PROJECT_ROOT / "data" / "prep" / "scaler.joblib")
        return model, scaler
    except Exception as e:
        logger.error(f"Error cargando modelo o scaler: {str(e)}")
        raise


def generate_predictions():
    """
    Genera predicciones usando el modelo entrenado.
    """
    try:
        # 1. Cargar modelo y scaler
        logger.info("Cargando modelo y scaler...")
        model, scaler = load_model_and_scaler()

        # 2. Preparar features para test
        logger.info("Preparando features de test...")
        engineer = FeatureEngineer(PROJECT_ROOT / "data")
        sales_df, items_df, test_df = engineer.load_processed_data()

        # 3. Crear features de test
        test_features = engineer.create_all_features_for_test(
            test_df, sales_df, items_df
        )

        # 4. Escalar features
        X_test_scaled = scaler.transform(test_features)

        # 5. Realizar predicciones
        logger.info("Generando predicciones...")
        predictions = model.predict(X_test_scaled)
        predictions = np.expm1(predictions).clip(0, 20)

        # 6. Crear DataFrame de predicciones
        submission = pd.DataFrame({"ID": test_df.index, "item_cnt_month": predictions})

        # 7. Guardar predicciones
        predictions_path = PROJECT_ROOT / "data" / "predictions"
        predictions_path.mkdir(exist_ok=True)

        output_file = (
            predictions_path
            / f"predictions_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        )
        submission.to_csv(output_file, index=False)

        logger.info(f"✅ Predicciones guardadas en: {output_file}")
        logger.info("\nEstadísticas de predicciones:")
        logger.info(f"Media: {predictions.mean():.4f}")
        logger.info(f"Desv. Est.: {predictions.std():.4f}")
        logger.info(f"Min: {predictions.min():.4f}")
        logger.info(f"Max: {predictions.max():.4f}")

    except Exception as e:
        logger.error(f"❌ Error en predicciones: {str(e)}")
        raise


def main():
    """Función principal para ejecutar las predicciones"""
    try:
        generate_predictions()
    except Exception as e:
        logger.error(f"Error en main: {str(e)}")
        raise


if __name__ == "__main__":
    main()
