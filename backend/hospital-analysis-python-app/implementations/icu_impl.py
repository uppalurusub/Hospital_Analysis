"""
icu_impl.py

ICU Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List
import pandas as pd
import numpy as np


class ICUAnalyticsImpl:

    DISEASE_MAPPING = {
        "Hypertension": "dx_hypertension",
        "Type 2 Diabetes": "dx_type2_diabetes",
        "Heart Failure": "dx_heart_failure",
        "Coronary Artery Disease": "dx_coronary_artery_disease",
        "Chronic Kidney Disease": "dx_chronic_kidney_disease",
        "COPD": "dx_copd",
        "Asthma": "dx_asthma"
    }

    def __init__(
        self,
        patients_df: pd.DataFrame,
        outcomes_df: pd.DataFrame
    ):

        self.patients_df = patients_df.copy()
        self.outcomes_df = outcomes_df.copy()

        self.df = pd.merge(
            self.patients_df,
            self.outcomes_df,
            on="patient_id",
            how="inner"
        )

    # =====================================================
    # Helper
    # =====================================================

    def _safe_float(self, value):

        if pd.isna(value):
            return 0.0

        if value in [np.inf, -np.inf]:
            return 0.0

        return float(value)

    # =====================================================
    # ICU Admission Rate
    # =====================================================

    def icu_admission_rate(self) -> Dict:

        total_admissions = int(len(self.df))

        icu_admissions = int(
            self.df["icu_admission"]
            .fillna(0)
            .sum()
        )

        rate = (
            round(
                icu_admissions * 100 /
                total_admissions,
                2
            )
            if total_admissions > 0
            else 0.0
        )

        return {
            "total_admissions": total_admissions,
            "icu_admissions": icu_admissions,
            "icu_admission_rate_pct": rate
        }

    # =====================================================
    # Average ICU Days
    # =====================================================

    def average_icu_days(self) -> Dict:

        icu_df = self.df[
            self.df["icu_admission"] == 1
        ]

        avg_days = round(
            self._safe_float(
                icu_df["icu_days"].mean()
            ),
            2
        )

        return {
            "average_icu_days": avg_days
        }

    # =====================================================
    # ICU Utilization By Age
    # =====================================================

    def icu_by_age_group(self) -> List[Dict]:

        df = self.df.copy()

        bins = [0, 18, 35, 50, 65, 80, 120]

        labels = [
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "66-80",
            "80+"
        ]

        df["age_group"] = pd.cut(
            df["age"],
            bins=bins,
            labels=labels
        )

        result = (
            df.groupby(
                "age_group",
                observed=False
            )["icu_admission"]
            .mean()
            .reset_index()
        )

        result["icu_rate_pct"] = (
            result["icu_admission"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "age_group",
                    "icu_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # ICU By Gender
    # =====================================================

    def icu_by_gender(self) -> List[Dict]:

        result = (
            self.df.groupby("sex")
            ["icu_admission"]
            .mean()
            .reset_index()
        )

        result["icu_rate_pct"] = (
            result["icu_admission"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "sex",
                    "icu_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # ICU By Charlson Risk
    # =====================================================

    def icu_by_charlson(self) -> List[Dict]:

        df = self.df.copy()

        bins = [-1, 1, 3, 5, 100]

        labels = [
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]

        df["risk_group"] = pd.cut(
            df["charlson_index"],
            bins=bins,
            labels=labels
        )

        result = (
            df.groupby(
                "risk_group",
                observed=False
            )["icu_admission"]
            .mean()
            .reset_index()
        )

        result["icu_rate_pct"] = (
            result["icu_admission"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "risk_group",
                    "icu_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # ICU By Disease
    # =====================================================

    def icu_by_disease(self) -> List[Dict]:

        results = []

        for disease, column in self.DISEASE_MAPPING.items():

            if column not in self.df.columns:
                continue

            disease_df = self.df[
                self.df[column] == 1
            ]

            icu_rate = round(
                self._safe_float(
                    disease_df[
                        "icu_admission"
                    ].mean()
                ) * 100,
                2
            )

            results.append({
                "disease": disease,
                "icu_rate_pct": icu_rate
            })

        return sorted(
            results,
            key=lambda x: x["icu_rate_pct"],
            reverse=True
        )

    # =====================================================
    # High ICU Risk Patients
    # =====================================================

    def high_icu_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        df = self.df.copy()

        df["icu_risk_score"] = (
            (df["charlson_index"] * 5)
            +
            (df["age"] / 10)
            +
            (df["heart_rate"] / 20)
            +
            (df["systolic_bp"] / 20)
        )

        result = (
            df.sort_values(
                "icu_risk_score",
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
                    "heart_rate",
                    "icu_risk_score"
                ]
            ]
            .round(2)
            .to_dict("records")
        )

    # =====================================================
    # ICU Risk Summary
    # =====================================================

    def icu_risk_summary(self) -> Dict:

        return {
            "icu_admission_rate":
                self.icu_admission_rate(),

            "average_icu_days":
                self.average_icu_days(),

            "top_icu_diseases":
                self.icu_by_disease()[:5]
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(self) -> Dict:

        return {
            "icu_admission_rate":
                self.icu_admission_rate(),

            "average_icu_days":
                self.average_icu_days(),

            "icu_by_age":
                self.icu_by_age_group(),

            "icu_by_gender":
                self.icu_by_gender(),

            "icu_by_charlson":
                self.icu_by_charlson(),

            "top_icu_diseases":
                self.icu_by_disease()[:5]
        }