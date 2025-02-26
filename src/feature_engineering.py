"""
Módulo para la ingeniería de features del modelo de predicción de ventas.

Este módulo contiene las funciones y clases necesarias para transformar
los datos procesados en features útiles para el modelo.
"""

from pathlib import Path
import logging
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

logger = logging.getLogger(__name__)


class FeatureEngineer:
    """
    Clase para la creación y transformación de features.

    Attributes:
        data_path (Path): Ruta base para los datos
        scaler (StandardScaler): Scaler para normalizar features
    """

    def __init__(self, data_path: Path):
        """
        Inicializa el ingeniero de features.

        Args:
            data_path (Path): Ruta base donde se encuentran los datos
        """
        self.data_path = data_path
        self.prep_path = data_path / "processed"
        self.scaler = StandardScaler()

    def _get_feature_columns(self) -> list:
        """Retorna la lista de columnas de features."""
        return [
            "sales_ema_2m",
            "hierarchical_ma_interaction",
            "trend_2m",
            "sales_volatility",
            "category_avg",
            "trend_volatility_ratio",
        ]

    def load_processed_data(self) -> tuple:
        """
        Carga los datos procesados.

        Returns:
            tuple: (sales_df, items_df, test_df) DataFrames procesados
        """
        try:
            logger.info("Cargando datos procesados...")
            sales_df = pd.read_csv(self.prep_path / "sales_processed.csv")
            items_df = pd.read_csv(self.prep_path / "items_processed.csv")
            test_df = pd.read_csv(self.prep_path / "test_processed.csv")

            return sales_df, items_df, test_df

        except Exception as e:
            logger.error(f"Error cargando datos procesados: {str(e)}")
            raise

    def create_time_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Crea features basadas en tiempo.

        Args:
            df (pd.DataFrame): DataFrame con columna 'date'

        Returns:
            pd.DataFrame: DataFrame con nuevas features temporales
        """
        df["date"] = pd.to_datetime(df["date"])
        group_cols = ["shop_id", "item_id"]
        
        df["sales_ema_2m"] = (
            df.groupby(group_cols)["item_cnt_day"]
            .transform(lambda x: x.ewm(span=2, adjust=False).mean())
            .fillna(0)
        )
        return df

    def create_price_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Crea features basadas en precio.

        Args:
            df (pd.DataFrame): DataFrame con columna 'item_price'

        Returns:
            pd.DataFrame: DataFrame con nuevas features de precio
        """
        group_cols = ["shop_id", "item_id"]
        
        df["trend_2m"] = (
            df.groupby(group_cols)["item_price"]
            .transform(lambda x: x.rolling(2, min_periods=1).mean())
            .fillna(0)
        )
        
        df["sales_volatility"] = (
            df.groupby(group_cols)["item_cnt_day"]
            .transform(lambda x: x.rolling(3, min_periods=1).std())
            .fillna(0)
        )
        return df

    def create_category_features(
        self, df: pd.DataFrame, items_df: pd.DataFrame, is_train: bool = True
    ) -> pd.DataFrame:
        """
        Crea features basadas en categorías.

        Args:
            df (pd.DataFrame): DataFrame principal
            items_df (pd.DataFrame): DataFrame de items
            is_train (bool): Indica si los datos son de entrenamiento

        Returns:
            pd.DataFrame: DataFrame con nuevas features de categoría
        """
        # Merge con categorías
        df = df.merge(
            items_df[["item_id", "item_category_id"]], on="item_id", how="left"
        )

        if is_train:
            # Para datos de entrenamiento
            df["category_avg"] = df.groupby("item_category_id")[
                "item_cnt_day"
            ].transform("mean")
        else:
            # Para datos de test, usar estadísticas históricas
            category_stats = items_df.groupby("item_category_id").size().reset_index()
            category_stats.columns = ["item_category_id", "category_count"]
            df["category_avg"] = (
                df["item_category_id"]
                .map(category_stats.set_index("item_category_id")["category_count"])
                .fillna(0)
            )

        return df

    def create_all_features(self) -> tuple:
        """
        Crea todas las features y prepara datos para entrenamiento.

        Returns:
            tuple: (X, y) Features y target para entrenamiento
        """
        try:
            # 1. Cargar datos
            sales_df, items_df, _ = self.load_processed_data()

            # 2. Crear features
            df = sales_df.pipe(self.create_time_features)
            df = self.create_price_features(df)
            df = self.create_category_features(df, items_df)

            # 3. Crear features finales
            df["trend_volatility_ratio"] = df["trend_2m"] / df["sales_volatility"].clip(
                lower=0.001
            )
            df["hierarchical_ma_interaction"] = (
                df["category_avg"] * df["sales_ema_2m"] * df["trend_2m"]
            )

            # 4. Seleccionar features finales
            feature_cols = self._get_feature_columns()

            X = df[feature_cols]
            y = df["item_cnt_log"]

            # 5. Escalar features
            X_scaled = self.scaler.fit_transform(X)

            # 6. Guardar scaler
            joblib.dump(self.scaler, self.prep_path / "scaler.joblib")

            # 7. Guardar datos preparados
            pd.DataFrame(X_scaled, columns=feature_cols).to_csv(
                self.prep_path / "X_train_scaled.csv", index=False
            )
            y.to_csv(self.prep_path / "y_train.csv", index=False)

            logger.info("✅ Features creadas exitosamente!")
            return X_scaled, y

        except Exception as e:
            logger.error(f"❌ Error creando features: {str(e)}")
            raise

    def create_all_features_for_test(
        self, test_df: pd.DataFrame, sales_df: pd.DataFrame, items_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Crea features para el conjunto de test.

        Args:
            test_df: DataFrame de test
            sales_df: DataFrame de ventas históricas
            items_df: DataFrame de items

        Returns:
            pd.DataFrame: Features preparadas para test
        """
        try:
            # 1. Crear features temporales usando datos históricos
            historical_stats = (
                sales_df.groupby(["shop_id", "item_id"])
                .agg({"item_cnt_day": ["mean", "std"], "item_price": ["mean", "std"]})
                .reset_index()
            )

            historical_stats.columns = [
                "shop_id",
                "item_id",
                "sales_mean",
                "sales_std",
                "price_mean",
                "price_std",
            ]

            # 2. Merge con datos de test
            df = test_df.merge(historical_stats, on=["shop_id", "item_id"], how="left")

            # 3. Crear features
            df["sales_ema_2m"] = df["sales_mean"].fillna(0)
            df["trend_2m"] = df["price_mean"].fillna(0)
            df["sales_volatility"] = df["sales_std"].fillna(0)

            # 4. Features de categoría (indicando que es test)
            df = self.create_category_features(df, items_df, is_train=False)

            # 5. Ratios e interacciones
            df["trend_volatility_ratio"] = df["trend_2m"] / df["sales_volatility"].clip(
                lower=0.001
            )
            df["hierarchical_ma_interaction"] = (
                df["category_avg"] * df["sales_ema_2m"] * df["trend_2m"]
            )

            # 6. Seleccionar features finales
            feature_cols = self._get_feature_columns()

            return df[feature_cols]

        except Exception as e:
            logger.error(f"Error creando features de test: {str(e)}")
            raise
