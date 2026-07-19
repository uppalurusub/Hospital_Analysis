"""
cost_impl.py

Healthcare Cost Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List

import numpy as np
import pandas as pd


class CostAnalyticsImpl:

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
    # Average Cost
    # =====================================================

    def average_cost(self) -> Dict:

        avg_cost = round(
            self._safe_float(
                self.df["total_charges_usd"].mean()
            ),
            2
        )

        return {
            "average_cost_per_admission_usd":
                avg_cost
        }

    # =====================================================
    # Median Cost
    # =====================================================

    def median_cost(self) -> Dict:

        median_cost = round(
            self._safe_float(
                self.df["total_charges_usd"].median()
            ),
            2
        )

        return {
            "median_cost_per_admission_usd":
                median_cost
        }

    # =====================================================
    # Total Cost
    # =====================================================

    def total_cost(self) -> Dict:

        total_cost = round(
            self._safe_float(
                self.df["total_charges_usd"].sum()
            ),
            2
        )

        return {
            "total_hospital_cost_usd":
                total_cost
        }

    # =====================================================
    # Cost By Age Group
    # =====================================================

    def cost_by_age_group(self) -> List[Dict]:

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
            )["total_charges_usd"]
            .mean()
            .reset_index()
        )

        result["average_cost_usd"] = (
            result["total_charges_usd"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "age_group",
                    "average_cost_usd"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Cost By Gender
    # =====================================================

    def cost_by_gender(self) -> List[Dict]:

        result = (
            self.df.groupby("sex")
            ["total_charges_usd"]
            .mean()
            .reset_index()
        )

        result["average_cost_usd"] = (
            result["total_charges_usd"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "sex",
                    "average_cost_usd"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Cost By Disease
    # =====================================================

    def cost_by_disease(self) -> List[Dict]:

        results = []

        for disease, column in self.DISEASE_MAPPING.items():

            if column not in self.df.columns:
                continue

            disease_df = self.df[
                self.df[column] == 1
            ]

            avg_cost = round(
                self._safe_float(
                    disease_df[
                        "total_charges_usd"
                    ].mean()
                ),
                2
            )

            results.append({
                "disease": disease,
                "average_cost_usd": avg_cost
            })

        return sorted(
            results,
            key=lambda x:
            x["average_cost_usd"],
            reverse=True
        )

    # =====================================================
    # Cost By Charlson Risk
    # =====================================================

    def cost_by_charlson(self) -> List[Dict]:

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
            )["total_charges_usd"]
            .mean()
            .reset_index()
        )

        result["average_cost_usd"] = (
            result["total_charges_usd"]
            .fillna(0)
            .round(2)
        )

        return (
            result[
                [
                    "risk_group",
                    "average_cost_usd"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Cost By ICU
    # =====================================================

    def cost_by_icu(self) -> Dict:

        icu_df = self.df[
            self.df["icu_admission"] == 1
        ]

        non_icu_df = self.df[
            self.df["icu_admission"] == 0
        ]

        icu_cost = round(
            self._safe_float(
                icu_df[
                    "total_charges_usd"
                ].mean()
            ),
            2
        )

        non_icu_cost = round(
            self._safe_float(
                non_icu_df[
                    "total_charges_usd"
                ].mean()
            ),
            2
        )

        return {
            "icu_average_cost_usd":
                icu_cost,

            "non_icu_average_cost_usd":
                non_icu_cost
        }

    # =====================================================
    # Cost By LOS
    # =====================================================

    def cost_los_analysis(self) -> Dict:

        correlation = self._safe_float(
            self.df[
                [
                    "length_of_stay_days",
                    "total_charges_usd"
                ]
            ]
            .corr()
            .iloc[0, 1]
        )

        return {
            "los_cost_correlation":
                round(correlation, 4)
        }

    # =====================================================
    # High Cost Patients
    # =====================================================

    def high_cost_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        result = (
            self.df.sort_values(
                "total_charges_usd",
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
                    "icu_admission",
                    "total_charges_usd"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Cost Summary
    # =====================================================

    def cost_summary(self) -> Dict:

        return {
            "average_cost":
                self.average_cost(),

            "median_cost":
                self.median_cost(),

            "total_cost":
                self.total_cost(),

            "cost_by_icu":
                self.cost_by_icu(),

            "los_analysis":
                self.cost_los_analysis()
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(self) -> Dict:

        return {
            "average_cost":
                self.average_cost(),

            "median_cost":
                self.median_cost(),

            "total_cost":
                self.total_cost(),

            "cost_by_charlson":
                self.cost_by_charlson(),

            "cost_by_icu":
                self.cost_by_icu(),

            "top_cost_patients":
                self.high_cost_patients(10)
        }