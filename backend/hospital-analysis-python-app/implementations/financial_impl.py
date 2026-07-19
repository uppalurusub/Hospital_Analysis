import pandas as pd

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from visualizations.financial_visualization_impl import (
    FinancialVisualization
)


class FinancialImplementation:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        outcomes_df = datasets["outcomes"]

        diagnoses_df = datasets["diagnoses"]

        # ====================================
        # Average Cost per Admission
        # ====================================

        avg_cost_per_admission = round(
            float(
                outcomes_df[
                    "total_charges_usd"
                ].mean()
            ),
            2
        )

        # ====================================
        # Cost per DRG
        # ====================================

        drg_df = (
            outcomes_df
            .groupby("primary_drg")
            .agg(
                avg_cost=(
                    "total_charges_usd",
                    "mean"
                ),
                admissions=(
                    "patient_id",
                    "count"
                )
            )
            .reset_index()
            .sort_values(
                "avg_cost",
                ascending=False
            )
        )

        # ====================================
        # Cost per Diagnosis
        # ====================================

        merged_df = (
            outcomes_df
            .merge(
                diagnoses_df[
                    [
                        "patient_id",
                        "primary_diagnosis"
                    ]
                ],
                on="patient_id",
                how="left"
            )
        )

        diagnosis_df = (
            merged_df
            .groupby(
                "primary_diagnosis"
            )
            .agg(
                avg_cost=(
                    "total_charges_usd",
                    "mean"
                )
            )
            .reset_index()
            .sort_values(
                "avg_cost",
                ascending=False
            )
        )

        # ====================================
        # Cost per Readmission
        # ====================================

        readmission_cost = round(
            float(
                outcomes_df.loc[
                    outcomes_df[
                        "readmitted_30d"
                    ] == 1,
                    "total_charges_usd"
                ].mean()
            ),
            2
        )

        # ====================================
        # High Cost Patient Rate
        # ====================================

        threshold = (
            outcomes_df[
                "total_charges_usd"
            ].quantile(0.90)
        )

        high_cost_rate = round(
            (
                (
                    outcomes_df[
                        "total_charges_usd"
                    ] > threshold
                ).sum()
                /
                len(outcomes_df)
            ) * 100,
            2
        )

        kpi_df = pd.DataFrame(
            [
                {
                    "metric":
                    "Avg Cost / Admission",
                    "value":
                    round(
                        avg_cost_per_admission,
                        2
                    )
                },
                {
                    "metric":
                    "Cost / Readmission",
                    "value":
                    readmission_cost
                },
                {
                    "metric":
                    "High Cost Patient %",
                    "value":
                    high_cost_rate
                }
            ]
        )

        return (
            FinancialVisualization
            .generate_dashboard(
                outcomes_df,
                drg_df,
                diagnosis_df,
                kpi_df
            )
        )