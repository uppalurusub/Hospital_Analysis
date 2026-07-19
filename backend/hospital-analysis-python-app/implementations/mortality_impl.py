"""
mortality_impl.py

Mortality Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List
import pandas as pd
import numpy as np


class MortalityAnalyticsImpl:

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
        "Anxiety": "dx_anxiety",
        "Hypothyroidism": "dx_hypothyroidism",
        "Osteoarthritis": "dx_osteoarthritis"
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
    # Mortality Rate
    # =====================================================

    def mortality_rate(self) -> Dict:

        total_admissions = int(len(self.df))

        deaths = int(
            self.df["in_hospital_death"]
            .fillna(0)
            .sum()
        )

        mortality_rate = (
            round(
                deaths * 100 / total_admissions,
                2
            )
            if total_admissions > 0
            else 0.0
        )

        return {
            "total_admissions": total_admissions,
            "deaths": deaths,
            "mortality_rate_pct": mortality_rate
        }

    # =====================================================
    # Mortality By Age Group
    # =====================================================

    def mortality_by_age_group(self) -> List[Dict]:

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
            )["in_hospital_death"]
            .mean()
            .reset_index()
        )

        result["mortality_rate_pct"] = (
            result["in_hospital_death"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "age_group",
                    "mortality_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Mortality By Gender
    # =====================================================

    def mortality_by_gender(self) -> List[Dict]:

        result = (
            self.df.groupby(
                "sex"
            )["in_hospital_death"]
            .mean()
            .reset_index()
        )

        result["mortality_rate_pct"] = (
            result["in_hospital_death"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "sex",
                    "mortality_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Mortality By Charlson
    # =====================================================

    def mortality_by_charlson(self) -> List[Dict]:

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
            )["in_hospital_death"]
            .mean()
            .reset_index()
        )

        result["mortality_rate_pct"] = (
            result["in_hospital_death"]
            .fillna(0)
            * 100
        ).round(2)

        return (
            result[
                [
                    "risk_group",
                    "mortality_rate_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Mortality By ICU
    # =====================================================

    def mortality_by_icu(self) -> Dict:

        icu = self.df[
            self.df["icu_admission"] == 1
        ]

        non_icu = self.df[
            self.df["icu_admission"] == 0
        ]

        icu_rate = (
            round(
                self._safe_float(
                    icu["in_hospital_death"]
                    .mean()
                ) * 100,
                2
            )
        )

        non_icu_rate = (
            round(
                self._safe_float(
                    non_icu["in_hospital_death"]
                    .mean()
                ) * 100,
                2
            )
        )

        return {
            "icu_mortality_rate_pct":
                icu_rate,

            "non_icu_mortality_rate_pct":
                non_icu_rate
        }

    # =====================================================
    # Mortality By Disease
    # =====================================================

    def mortality_by_disease(self) -> List[Dict]:

        results = []

        for disease, column in self.DISEASE_MAPPING.items():

            if column not in self.df.columns:
                continue

            disease_df = self.df[
                self.df[column] == 1
            ]

            mortality_rate = (
                round(
                    self._safe_float(
                        disease_df[
                            "in_hospital_death"
                        ].mean()
                    ) * 100,
                    2
                )
            )

            results.append({
                "disease": disease,
                "mortality_rate_pct":
                    mortality_rate
            })

        results.sort(
            key=lambda x:
            x["mortality_rate_pct"],
            reverse=True
        )

        return results

    # =====================================================
    # High Risk Patients
    # =====================================================

    def high_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        df = self.df.copy()

        df["mortality_risk_score"] = (
            (df["charlson_index"] * 5)
            +
            (df["age"] / 10)
            +
            (df["length_of_stay_days"] * 2)
            +
            (df["icu_admission"] * 10)
        )

        result = (
            df.sort_values(
                "mortality_risk_score",
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
                    "icu_admission",
                    "mortality_risk_score"
                ]
            ]
            .round(2)
            .to_dict("records")
        )

    # =====================================================
    # Risk Summary
    # =====================================================

    def risk_summary(self) -> Dict:

        return {
            "mortality_rate":
                self.mortality_rate(),

            "icu_analysis":
                self.mortality_by_icu(),

            "top_disease_risks":
                self.mortality_by_disease()[:5]
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(self) -> Dict:

        return {
            "overall_mortality":
                self.mortality_rate(),

            "mortality_by_icu":
                self.mortality_by_icu(),

            "mortality_by_gender":
                self.mortality_by_gender(),

            "mortality_by_age":
                self.mortality_by_age_group(),

            "high_risk_patients":
                self.high_risk_patients(10)
        }