import pandas as pd

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from visualizations.clinical_risk_visualization_impl import (
    ClinicalRiskVisualization
)


class ClinicalRiskImplementation:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        labs_df = datasets["labs"]

        medications_df = datasets["medications"]

        total_patients = int(
            patients_df["patient_id"]
            .nunique()
        )

        # High BP

        high_bp = int(
            (
                (
                    patients_df["systolic_bp"] >= 140
                )
                |
                (
                    patients_df["diastolic_bp"] >= 90
                )
            ).sum()
        )

        high_bp_rate = round(
            high_bp / total_patients * 100,
            2
        )

        # Obesity

        obesity_rate = round(
            (
                (
                    patients_df["bmi"] >= 30
                ).sum()
                / total_patients
            ) * 100,
            2
        )

        # Tachycardia

        tachycardia_rate = round(
            (
                (
                    patients_df["heart_rate"] > 100
                ).sum()
                / total_patients
            ) * 100,
            2
        )

        # Abnormal Labs

        abnormal_lab_rate = round(
            (
                labs_df["is_abnormal"]
                .fillna(0)
                .sum()
                /
                len(labs_df)
            ) * 100,
            2
        )

        # Medication Non-Adherence

        non_adherence_rate = round(
            (
                (
                    medications_df[
                        "adherence_pct"
                    ] < 80
                ).sum()
                /
                len(medications_df)
            ) * 100,
            2
        )

        kpi_df = pd.DataFrame(
            [
                {
                    "risk_metric":
                        "High BP",
                    "rate":
                        high_bp_rate
                },
                {
                    "risk_metric":
                        "Obesity",
                    "rate":
                        obesity_rate
                },
                {
                    "risk_metric":
                        "Tachycardia",
                    "rate":
                        tachycardia_rate
                },
                {
                    "risk_metric":
                        "Abnormal Labs",
                    "rate":
                        abnormal_lab_rate
                },
                {
                    "risk_metric":
                        "Medication Non-Adherence",
                    "rate":
                        non_adherence_rate
                }
            ]
        )

        return (
            ClinicalRiskVisualization
            .generate_dashboard(
                kpi_df
            )
        )