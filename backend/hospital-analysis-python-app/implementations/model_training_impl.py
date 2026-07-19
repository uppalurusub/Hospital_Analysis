from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    mean_absolute_error,
    r2_score
)


class ModelTraining:

    @staticmethod
    def classification_model(
            df,
            features,
            target
    ):
        model_df = df[
            features + [target]
        ].copy()

        model_df = model_df.dropna(
            subset=[target]
        )

        X = model_df[features]

        y = model_df[target]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42
            )
        )

        model = (
            RandomForestClassifier(
                n_estimators=200,
                random_state=42
            )
        )

        

        model.fit(
            X_train,
            y_train
        )

        predictions = (
            model.predict(X_test)
        )

        accuracy = round(
            accuracy_score(
                y_test,
                predictions
            ),
            4
        )

        return {
            "model": model,
            "accuracy": accuracy
        }

    @staticmethod
    def regression_model(
            df,
            features,
            target
    ):
        model_df = df[
            features + [target]
        ].copy()

        model_df = model_df.dropna(
            subset=[target]
        )

        X = model_df[features]

        y = model_df[target]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.20,
                random_state=42
            )
        )

        model = (
            RandomForestRegressor(
                n_estimators=200,
                random_state=42
            )
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = (
            model.predict(X_test)
        )

        mae = round(
            mean_absolute_error(
                y_test,
                predictions
            ),
            2
        )

        r2 = round(
            r2_score(
                y_test,
                predictions
            ),
            4
        )

        return {
            "model": model,
            "mae": mae,
            "r2": r2
        }