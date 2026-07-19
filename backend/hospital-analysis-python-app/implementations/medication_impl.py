"""
medication_impl.py

Medication Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List

import numpy as np
import pandas as pd


class MedicationAnalyticsImpl:

    def __init__(
        self,
        medications_df: pd.DataFrame
    ):

        self.df = medications_df.copy()

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
    # Overall Adherence Rate
    # =====================================================

    def adherence_rate(self) -> Dict:

        adherence = round(
            self._safe_float(
                self.df["adherence_pct"].mean()
            ),
            2
        )

        return {
            "overall_adherence_pct": adherence
        }

    # =====================================================
    # Non-Adherence Rate
    # =====================================================

    def non_adherence_rate(self) -> Dict:

        non_adherent = self.df[
            self.df["adherence_pct"] < 80
        ]

        total_patients = len(self.df)

        rate = (
            round(
                (len(non_adherent) * 100)
                / total_patients,
                2
            )
            if total_patients > 0
            else 0.0
        )

        return {
            "non_adherence_rate_pct": rate,
            "non_adherent_records":
                int(len(non_adherent))
        }

    # =====================================================
    # Top Medications
    # =====================================================

    def top_medications(
        self,
        top_n: int = 10
    ) -> List[Dict]:

        result = (
            self.df.groupby(
                "medication"
            )
            .size()
            .reset_index(
                name="prescription_count"
            )
            .sort_values(
                "prescription_count",
                ascending=False
            )
            .head(top_n)
        )

        return result.to_dict("records")

    # =====================================================
    # Adherence By Medication
    # =====================================================

    def adherence_by_medication(
        self
    ) -> List[Dict]:

        result = (
            self.df.groupby(
                "medication"
            )["adherence_pct"]
            .mean()
            .reset_index()
        )

        result["average_adherence_pct"] = (
            result["adherence_pct"]
            .fillna(0)
            .round(2)
        )

        result = result.sort_values(
            "average_adherence_pct"
        )

        return (
            result[
                [
                    "medication",
                    "average_adherence_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Adherence By Indication
    # =====================================================

    def adherence_by_indication(
        self
    ) -> List[Dict]:

        result = (
            self.df.groupby(
                "indication"
            )["adherence_pct"]
            .mean()
            .reset_index()
        )

        result["average_adherence_pct"] = (
            result["adherence_pct"]
            .fillna(0)
            .round(2)
        )

        result = result.sort_values(
            "average_adherence_pct"
        )

        return (
            result[
                [
                    "indication",
                    "average_adherence_pct"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Generic Vs Brand
    # =====================================================

    def generic_vs_brand(
        self
    ) -> Dict:

        generic_df = self.df[
            self.df["is_generic"] == 1
        ]

        brand_df = self.df[
            self.df["is_generic"] == 0
        ]

        generic_adherence = round(
            self._safe_float(
                generic_df[
                    "adherence_pct"
                ].mean()
            ),
            2
        )

        brand_adherence = round(
            self._safe_float(
                brand_df[
                    "adherence_pct"
                ].mean()
            ),
            2
        )

        return {
            "generic_adherence_pct":
                generic_adherence,

            "brand_adherence_pct":
                brand_adherence,

            "generic_prescriptions":
                int(len(generic_df)),

            "brand_prescriptions":
                int(len(brand_df))
        }

    # =====================================================
    # High Risk Non-Adherent Patients
    # =====================================================

    def high_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        result = (
            self.df.sort_values(
                "adherence_pct",
                ascending=True
            )
            .head(top_n)
        )

        return (
            result[
                [
                    "patient_id",
                    "medication",
                    "indication",
                    "adherence_pct",
                    "dose",
                    "frequency"
                ]
            ]
            .to_dict("records")
        )

    # =====================================================
    # Medication Summary
    # =====================================================

    def medication_summary(
        self
    ) -> Dict:

        return {
            "adherence_rate":
                self.adherence_rate(),

            "non_adherence_rate":
                self.non_adherence_rate(),

            "generic_vs_brand":
                self.generic_vs_brand(),

            "top_medications":
                self.top_medications(5)
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(
        self
    ) -> Dict:

        return {
            "adherence_rate":
                self.adherence_rate(),

            "non_adherence_rate":
                self.non_adherence_rate(),

            "generic_vs_brand":
                self.generic_vs_brand(),

            "top_medications":
                self.top_medications(10),

            "worst_adherence_medications":
                self.adherence_by_medication()[:10],

            "high_risk_patients":
                self.high_risk_patients(10)
        }