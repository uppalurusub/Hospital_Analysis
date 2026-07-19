"""
readmission_impl.py

Readmission Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List
import pandas as pd
from utils.safe_float import safe_float

class ReadmissionAnalyticsImpl:

    def __init__(
        self,
        patients_df: pd.DataFrame,
        outcomes_df: pd.DataFrame,
        medications_df: pd.DataFrame = None
    ):

        self.patients_df = patients_df.copy()
        self.outcomes_df = outcomes_df.copy()

        self.medications_df = (
            medications_df.copy()
            if medications_df is not None
            else pd.DataFrame()
        )

    # =====================================================
    # Readmission Rate
    # =====================================================

    def readmission_rate(self) -> Dict:

        total_admissions = int(
            len(self.outcomes_df)
        )

        readmissions = int(
            self.outcomes_df[
                self.outcomes_df["readmitted_30d"] == 1
            ].shape[0]
        )

        rate = round(
            (readmissions / total_admissions) * 100,
            2
        ) if total_admissions > 0 else 0

        return {
            "total_admissions": total_admissions,
            "readmissions": readmissions,
            "readmission_rate_pct": float(rate)
        }

    # =====================================================
    # Average Days to Readmission
    # =====================================================

    def average_days_to_readmission(
        self
    ) -> Dict:

        readmitted = self.outcomes_df[
            self.outcomes_df["readmitted_30d"] == 1
        ]

        avg_days = round(
            safe_float(
                readmitted[
                    "days_to_readmission"
                ].mean()
            ),
            2
        ) if not readmitted.empty else 0

        return {
            "average_days_to_readmission":
                avg_days
        }

    # =====================================================
    # Readmission by Age Group
    # =====================================================

    def readmission_by_age_group(
        self
    ) -> List[Dict]:

        merged = pd.merge(
            self.outcomes_df,
            self.patients_df,
            on="patient_id",
            how="inner"
        )

        bins = [0, 18, 35, 50, 65, 80, 120]

        labels = [
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "66-80",
            "80+"
        ]

        merged["age_group"] = pd.cut(
            merged["age"],
            bins=bins,
            labels=labels
        )

        result = (
            merged.groupby(
                "age_group",
                observed=False
            )["readmitted_30d"]
            .mean()
            .reset_index()
        )

        result["readmission_rate_pct"] = (
            result["readmitted_30d"] * 100
        ).round(2)

        return (
            result[
                [
                    "age_group",
                    "readmission_rate_pct"
                ]
            ]
            .to_dict(
                orient="records"
            )
        )

    # =====================================================
    # Readmission by Charlson Index
    # =====================================================

    def readmission_by_charlson(
        self
    ) -> List[Dict]:

        merged = pd.merge(
            self.outcomes_df,
            self.patients_df,
            on="patient_id",
            how="inner"
        )

        bins = [-1, 1, 3, 5, 100]

        labels = [
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]

        merged["risk_group"] = pd.cut(
            merged["charlson_index"],
            bins=bins,
            labels=labels
        )

        result = (
            merged.groupby(
                "risk_group",
                observed=False
            )["readmitted_30d"]
            .mean()
            .reset_index()
        )

        result["readmission_rate_pct"] = (
            result["readmitted_30d"] * 100
        ).round(2)

        return (
            result[
                [
                    "risk_group",
                    "readmission_rate_pct"
                ]
            ]
            .to_dict(
                orient="records"
            )
        )

    # =====================================================
    # Readmission by Adherence
    # =====================================================

    def readmission_by_adherence(
        self
    ) -> Dict:

        if self.medications_df.empty:

            return {
                "message":
                    "Medication data unavailable"
            }

        adherence = (
            self.medications_df
            .groupby("patient_id")
            ["adherence_pct"]
            .mean()
            .reset_index()
        )

        merged = pd.merge(
            self.outcomes_df,
            adherence,
            on="patient_id",
            how="inner"
        )

        low_adherence = merged[
            merged["adherence_pct"] < 80
        ]

        high_adherence = merged[
            merged["adherence_pct"] >= 80
        ]

        low_rate = round(
            safe_float(
                low_adherence[
                    "readmitted_30d"
                ].mean() * 100
            ),
            2
        ) if not low_adherence.empty else 0

        high_rate = round(
            safe_float(
                high_adherence[
                    "readmitted_30d"
                ].mean() * 100
            ),
            2
        ) if not high_adherence.empty else 0

        return {
            "low_adherence_readmission_pct":
                low_rate,

            "high_adherence_readmission_pct":
                high_rate
        }

    # =====================================================
    # High Readmission Risk Patients
    # =====================================================

    def high_readmission_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        merged = pd.merge(
            self.outcomes_df,
            self.patients_df,
            on="patient_id",
            how="inner"
        )

        merged["risk_score"] = (
            (merged["charlson_index"] * 5)
            +
            (merged["age"] / 10)
            +
            (merged["length_of_stay_days"] * 2)
        )

        result = (
            merged.sort_values(
                "risk_score",
                ascending=False
            )
            .head(top_n)
        )

        return (
            result[
                [
                    "patient_id",
                    "age",
                    "charlson_index",
                    "length_of_stay_days",
                    "risk_score"
                ]
            ]
            .round(2)
            .to_dict(
                orient="records"
            )
        )

    # =====================================================
    # Readmission Risk Summary
    # =====================================================

    def readmission_risk_summary(
        self
    ) -> Dict:

        return {
            "overall_readmission":
                self.readmission_rate(),

            "average_days":
                self.average_days_to_readmission(),

            "adherence":
                self.readmission_by_adherence()
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(
        self
    ) -> Dict:

        return {
            "readmission_rate":
                self.readmission_rate(),

            "avg_days_to_readmission":
                self.average_days_to_readmission(),

            "age_group_analysis":
                self.readmission_by_age_group(),

            "charlson_analysis":
                self.readmission_by_charlson(),

            "adherence_analysis":
                self.readmission_by_adherence()
        }