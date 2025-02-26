"""
Script principal para el entrenamiento del modelo.
"""

from pathlib import Path
import sys
import logging
import joblib
import lightgbm as lgb
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error
import numpy as np
import argparse
from typing import Tuple, Optional

import pandas as pd
from sklearn.model_selection import train_test_split

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

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Train sales prediction model')
    parser.add_argument('--data-dir', type=str, default='data',
                      help='Directory containing input data')
    parser.add_argument('--model-dir', type=str, default='models',
                      help='Directory to save trained model')
    parser.add_argument('--model-name', type=str, default='model.joblib',
                      help='Name of the model file')
    return parser.parse_args()

def train_model(
    X: pd.DataFrame,
    y: pd.Series,
    params: dict
) -> tuple:
    """Entrena el modelo con los datos proporcionados."""
    try:
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = lgb.LGBMRegressor(**params)
        model.fit(X_train, y_train)
        score = model.score(X_val, y_val)
        return model, score
    except Exception as e:
        logger.error(f"Error en entrenamiento: {str(e)}")
        raise

def main():
    """Función principal para ejecutar el entrenamiento"""
    try:
        # Parsear argumentos
        args = parse_args()
        
        # 1. Configurar rutas
        data_path = Path(args.data_dir)
        models_path = Path(args.model_dir)
        models_path.mkdir(exist_ok=True)

        # 2. Crear features
        logger.info("Preparando features...")
        engineer = FeatureEngineer(data_path)
        X, y = engineer.create_all_features()

        # 3. Entrenar modelo
        model, score = train_model(X, y, {
            "n_estimators": 1000,
            "learning_rate": 0.05,
            "num_leaves": 31,
            "min_child_samples": 20,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "random_state": 42,
        })

        # 4. Guardar modelo
        model_path = models_path / args.model_name
        joblib.dump(model, model_path)
        logger.info(f"Modelo guardado en: {model_path}")
        logger.info(f"Score del modelo: {score:.4f}")

        logger.info("✅ Entrenamiento completado exitosamente!")

    except Exception as e:
        logger.error(f"❌ Error en entrenamiento: {str(e)}")
        raise

if __name__ == "__main__":
    main()
