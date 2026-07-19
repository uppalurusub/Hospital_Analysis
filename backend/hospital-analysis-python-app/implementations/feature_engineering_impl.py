import pandas as pd


class FeatureEngineering:

    @staticmethod
    def build_master_dataset(
            patients_df,
            outcomes_df,
            medications_df
    ):

        df = (
            patients_df
            .merge(
                outcomes_df,
                on="patient_id",
                how="left"
            )
        )

        adherence = (
            medications_df
            .groupby("patient_id")
            ["adherence_pct"]
            .mean()
            .reset_index()
        )

        df = (
            df.merge(
                adherence,
                on="patient_id",
                how="left"
            )
        )

        return df