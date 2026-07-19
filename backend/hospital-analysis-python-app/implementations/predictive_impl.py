import pandas as pd

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from implementations.feature_engineering_impl import (
    FeatureEngineering
)

from implementations.model_training_impl import (
    ModelTraining
)

from visualizations.predictive_visualization_impl import (
    PredictiveVisualization
)


class PredictiveImplementation:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        master_df = (
            FeatureEngineering
            .build_master_dataset(
                datasets["patients"],
                datasets["outcomes"],
                datasets["medications"]
            )
        )

        features = [
            "age",
            "bmi",
            "systolic_bp",
            "diastolic_bp",
            "heart_rate",
            "charlson_index"
        ]

        results = []

        # Readmission

        readmission = (
            ModelTraining
            .classification_model(
                master_df,
                features,
                "readmitted_30d"
            )
        )

        results.append(
            {
                "model":
                "Readmission",
                "score":
                readmission["accuracy"]
            }
        )

        # Mortality

        mortality = (
            ModelTraining
            .classification_model(
                master_df,
                features,
                "in_hospital_death"
            )
        )

        results.append(
            {
                "model":
                "Mortality",
                "score":
                mortality["accuracy"]
            }
        )

        # ICU

        icu = (
            ModelTraining
            .classification_model(
                master_df,
                features,
                "icu_admission"
            )
        )

        results.append(
            {
                "model":
                "ICU",
                "score":
                icu["accuracy"]
            }
        )

        # LOS

        los = (
            ModelTraining
            .regression_model(
                master_df,
                features,
                "length_of_stay_days"
            )
        )

        results.append(
            {
                "model":
                "LOS",
                "score":
                los["r2"]
            }
        )

        # Cost

        cost = (
            ModelTraining
            .regression_model(
                master_df,
                features,
                "total_charges_usd"
            )
        )

        results.append(
            {
                "model":
                "Cost",
                "score":
                cost["r2"]
            }
        )

        # Adherence

        adherence = (
            ModelTraining
            .regression_model(
                master_df,
                features,
                "adherence_pct"
            )
        )

        results.append(
            {
                "model":
                "Adherence",
                "score":
                adherence["r2"]
            }
        )

        metrics_df = pd.DataFrame(
            results
        )

        return (
            PredictiveVisualization
            .dashboard(
                metrics_df
            )
        )