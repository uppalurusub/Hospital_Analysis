"""
risk_impl.py

Clinical Risk Analytics Implementation Layer

Author: Healthcare Analytics Platform
"""

from typing import Dict, List
import pandas as pd


class RiskAnalyticsImpl:

    def __init__(
        self,
        patients_df: pd.DataFrame,
        lab_results_df: pd.DataFrame,
        medications_df: pd.DataFrame
    ):

        self.patients_df = patients_df.copy()
        self.lab_results_df = lab_results_df.copy()
        self.medications_df = medications_df.copy()

    # =====================================================
    # High Blood Pressure Rate
    # =====================================================

    def high_bp_rate(self) -> Dict:

        high_bp = self.patients_df[
            (self.patients_df["systolic_bp"] >= 140)
            |
            (self.patients_df["diastolic_bp"] >= 90)
        ]

        count = int(len(high_bp))

        total = int(len(self.patients_df))

        rate = round(
            (count / total) * 100,
            2
        )

        return {
            "high_bp_patients": count,
            "total_patients": total,
            "high_bp_rate_pct": float(rate)
        }

    # =====================================================
    # Obesity Rate
    # =====================================================

    def obesity_rate(self) -> Dict:

        obese = self.patients_df[
            self.patients_df["bmi"] >= 30
        ]

        count = int(len(obese))

        total = int(len(self.patients_df))

        rate = round(
            (count / total) * 100,
            2
        )

        return {
            "obese_patients": count,
            "obesity_rate_pct": float(rate)
        }

    # =====================================================
    # Tachycardia Rate
    # =====================================================

    def tachycardia_rate(self) -> Dict:

        tachycardia = self.patients_df[
            self.patients_df["heart_rate"] > 100
        ]

        count = int(len(tachycardia))

        total = int(len(self.patients_df))

        rate = round(
            (count / total) * 100,
            2
        )

        return {
            "tachycardia_patients": count,
            "tachycardia_rate_pct": float(rate)
        }

    # =====================================================
    # Abnormal Lab Rate
    # =====================================================

    def abnormal_lab_rate(self) -> Dict:

        abnormal = self.lab_results_df[
            self.lab_results_df["is_abnormal"] == 1
        ]

        abnormal_patients = int(
            abnormal["patient_id"].nunique()
        )

        total_patients = int(
            self.patients_df["patient_id"].nunique()
        )

        rate = round(
            (abnormal_patients / total_patients) * 100,
            2
        )

        return {
            "abnormal_lab_patients":
                abnormal_patients,

            "abnormal_lab_rate_pct":
                float(rate)
        }

    # =====================================================
    # Medication Non-Adherence
    # =====================================================

    def medication_non_adherence_rate(
        self
    ) -> Dict:

        non_adherent = self.medications_df[
            self.medications_df["adherence_pct"] < 80
        ]

        patient_count = int(
            non_adherent["patient_id"].nunique()
        )

        total_patients = int(
            self.medications_df["patient_id"]
            .nunique()
        )

        rate = round(
            (patient_count / total_patients) * 100,
            2
        )

        return {
            "non_adherent_patients":
                patient_count,

            "non_adherence_rate_pct":
                float(rate)
        }

    # =====================================================
    # Charlson Distribution
    # =====================================================

    def charlson_risk_distribution(
        self
    ) -> List[Dict]:

        bins = [-1, 1, 3, 5, 100]

        labels = [
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]

        df = self.patients_df.copy()

        df["risk_category"] = pd.cut(
            df["charlson_index"],
            bins=bins,
            labels=labels
        )

        result = (
            df["risk_category"]
            .value_counts()
            .reset_index()
        )

        result.columns = [
            "risk_category",
            "patient_count"
        ]

        return result.to_dict(
            orient="records"
        )

    # =====================================================
    # High Risk Patients
    # =====================================================

    def high_risk_patients(
        self,
        top_n: int = 20
    ) -> List[Dict]:

        df = self.patients_df.copy()

        df["risk_score"] = (
            (df["charlson_index"] * 5)
            +
            (df["bmi"] / 5)
            +
            (df["systolic_bp"] / 20)
            +
            (df["age"] / 10)
        )

        result = (
            df.sort_values(
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
                    "bmi",
                    "charlson_index",
                    "risk_score"
                ]
            ]
            .round(2)
            .to_dict(
                orient="records"
            )
        )

    # =====================================================
    # Risk Factor Summary
    # =====================================================

    def risk_factor_summary(
        self
    ) -> Dict:

        return {
            "high_bp":
                self.high_bp_rate(),

            "obesity":
                self.obesity_rate(),

            "tachycardia":
                self.tachycardia_rate(),

            "abnormal_labs":
                self.abnormal_lab_rate(),

            "non_adherence":
                self.medication_non_adherence_rate()
        }

    # =====================================================
    # Population Risk Score
    # =====================================================

    def population_risk_score(
        self
    ) -> Dict:

        df = self.patients_df.copy()

        df["risk_score"] = (
            (df["charlson_index"] * 5)
            +
            (df["bmi"] / 5)
            +
            (df["systolic_bp"] / 20)
            +
            (df["age"] / 10)
        )

        avg_score = round(
            float(
                df["risk_score"].mean()
            ),
            2
        )

        max_score = round(
            float(
                df["risk_score"].max()
            ),
            2
        )

        return {
            "average_population_risk_score":
                avg_score,

            "maximum_risk_score":
                max_score
        }

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def dashboard_kpis(
        self
    ) -> Dict:

        return {
            "high_bp":
                self.high_bp_rate(),

            "obesity":
                self.obesity_rate(),

            "tachycardia":
                self.tachycardia_rate(),

            "abnormal_labs":
                self.abnormal_lab_rate(),

            "medication_non_adherence":
                self.medication_non_adherence_rate(),

            "population_risk":
                self.population_risk_score()
        }