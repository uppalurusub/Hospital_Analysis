import pandas as pd

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from visualizations.outcomes_visualization_impl import (
    OutcomesVisualization
)


class OutcomesImplementation:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        outcomes_df = datasets["outcomes"]

        total_admissions = len(
            outcomes_df
        )

        # Mortality Rate

        mortality_rate = round(
            (
                outcomes_df[
                    "in_hospital_death"
                ]
                .fillna(0)
                .sum()
                /
                total_admissions
            ) * 100,
            2
        )

        # ICU Admission Rate

        icu_rate = round(
            (
                outcomes_df[
                    "icu_admission"
                ]
                .fillna(0)
                .sum()
                /
                total_admissions
            ) * 100,
            2
        )

        # Average ICU Days

        avg_icu_days = round(
            float(
                outcomes_df[
                    "icu_days"
                ].mean()
            ),
            2
        )

        # Readmission Rate

        readmission_rate = round(
            (
                outcomes_df[
                    "readmitted_30d"
                ]
                .fillna(0)
                .sum()
                /
                total_admissions
            ) * 100,
            2
        )

        # Average LOS

        avg_los = round(
            float(
                outcomes_df[
                    "length_of_stay_days"
                ].mean()
            ),
            2
        )

        kpi_df = pd.DataFrame(
            [
                {
                    "metric":
                    "Mortality Rate (%)",
                    "value":
                    mortality_rate
                },
                {
                    "metric":
                    "ICU Admission Rate (%)",
                    "value":
                    icu_rate
                },
                {
                    "metric":
                    "Average ICU Days",
                    "value":
                    avg_icu_days
                },
                {
                    "metric":
                    "Readmission Rate (%)",
                    "value":
                    readmission_rate
                },
                {
                    "metric":
                    "Average LOS",
                    "value":
                    avg_los
                }
            ]
        )

        discharge_df = (
            outcomes_df[
                "discharge_disposition"
            ]
            .value_counts()
            .reset_index()
        )

        discharge_df.columns = [
            "discharge_disposition",
            "count"
        ]

        return (
            OutcomesVisualization
            .generate_dashboard(
                outcomes_df,
                kpi_df,
                discharge_df
            )
        )