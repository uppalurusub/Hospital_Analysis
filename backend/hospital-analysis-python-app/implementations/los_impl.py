"""
los_impl.py

Length of Stay Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List

import numpy as np
import pandas as pd


class LOSAnalyticsImpl:

    DISEASE_MAPPING = {
        "Hypertension": "dx_hypertension",
        "Type 2 Diabetes": "dx_type2_diabetes",
        "Hyperlipidemia": "dx_hyperlipidemia",
        "Obesity": "dx_obesity",
        "Coronary Artery Disease": "dx_coronary_artery_disease",
        "Heart Failure": "dx_heart_failure",
        "Atrial Fibrillation": "dx_atrial_fibrillation",
        "Chronic Kidney Disease": "dx_chronic_kidney_disease",
        "COPD": "dx_copd",
        "Asthma": "dx_asthma",
        "Depression": "dx_depression",
        "Anxiety": "dx_anxiety"
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
    # Average LOS
    # =====================================================

    def average_los(self) -> Dict:

        avg_los = round(
            self._safe_float(
                self.df["length_of_stay_days"].mean()
            ),
            2
        )

        return {
            "average_los_days": avg_los
        }

    # =====================================================
    # Median LOS
    # =====================================================

    def median_los(self) -> Dict:

        median_los = round(
            self._safe_float(
                self.df["length_of_stay_days"].median()
            ),
            2
        )

        return {
            "median_los_days": median_los
        }

    # =====================================================
    # LOS By Age Group
    # =====================================================

    def los_by_age_group(self) -> List[Dict]:

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
            )["length_of_stay_days"]
            .mean()
            .reset_index()
        )

        result["average_los_days"] = (
            result["length_of_stay_days"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "age_group",
                    "average_los_days"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # LOS By Gender
    # =====================================================

    def los_by_gender(self) -> List[Dict]:

        result = (
            self.df.groupby("sex")
            ["length_of_stay_days"]
            .mean()
            .reset_index()
        )

        result["average_los_days"] = (
            result["length_of_stay_days"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "sex",
                    "average_los_days"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # LOS By Disease
    # =====================================================

    def los_by_disease(self) -> List[Dict]:

        results = []

        for disease, column in self.DISEASE_MAPPING.items():

            if column not in self.df.columns:
                continue

            disease_df = self.df[
                self.df[column] == 1
            ]

            avg_los = round(
                self._safe_float(
                    disease_df[
                        "length_of_stay_days"
                    ].mean()
                ),
                2
            )

            results.append({
                "disease": disease,
                "average_los_days": avg_los
            })

        return sorted(
            results,
            key=lambda x: x["average_los_days"],
            reverse=True
        )

    # =====================================================
    # LOS By Charlson Risk
    # =====================================================

    def los_by_charlson(self) -> List[Dict]:

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
            )["length_of_stay_days"]
            .mean()
            .reset_index()
        )

        result["average_los_days"] = (
            result["length_of_stay_days"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "risk_group",
                    "average_los_days"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # LOS By ICU Admission
    # =====================================================

    def los_by_icu(self) -> Dict:

        icu_df = self.df[
            self.df["icu_admission"] == 1
        ]

        non_icu_df = self.df[
            self.df["icu_admission"] == 0
        ]

        icu_los = round(
            self._safe_float(
                icu_df[
                    "length_of_stay_days"
                ].mean()
            ),
            2
        )

        non_icu_los = round(
            self._safe_float(
                non_icu_df[
                    "length_of_stay_days"
                ].mean()
            ),
            2
        )

        return {
            "icu_average_los_days": icu_los,
            "non_icu_average_los_days": non_icu_los
        }

    # =====================================================
    # Long Stay Patients
    # =====================================================

    def long_stay_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        result = (
            self.df.sort_values(
                "length_of_stay_days",
                ascending=False
            )
            .head(top_n)
        )

        return (
            result[
                [
                    "patient_id",
                    "age",
                    "length_of_stay_days",
                    "charlson_index",
                    "icu_admission"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # LOS Summary
    # =====================================================

    def los_summary(self) -> Dict:

        return {
            "average_los":
                self.average_los(),

            "median_los":
                self.median_los(),

            "los_by_icu":
                self.los_by_icu(),

            "top_los_diseases":
                self.los_by_disease()[:5]
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(self) -> Dict:

        return {
            "average_los":
                self.average_los(),

            "median_los":
                self.median_los(),

            "los_by_age":
                self.los_by_age_group(),

            "los_by_gender":
                self.los_by_gender(),

            "los_by_charlson":
                self.los_by_charlson(),

            "los_by_icu":
                self.los_by_icu(),

            "top_long_stay_patients":
                self.long_stay_patients(10)
        }