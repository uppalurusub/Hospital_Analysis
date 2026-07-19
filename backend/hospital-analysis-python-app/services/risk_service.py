"""
risk_service.py

Clinical Risk Analytics Service Layer

Responsibilities:
1. Load datasets
2. Validate datasets
3. Invoke implementation layer
4. Return JSON serializable responses

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd

from implementations.risk_impl import (
    RiskAnalyticsImpl
)


class RiskAnalyticsService:

    def __init__(
        self,
        patient_file_path: str,
        lab_file_path: str,
        medication_file_path: str
    ):

        self.patient_file_path = patient_file_path
        self.lab_file_path = lab_file_path
        self.medication_file_path = medication_file_path

        self.patients_df = self._load_csv(
            self.patient_file_path
        )

        self.lab_results_df = self._load_csv(
            self.lab_file_path
        )

        self.medications_df = self._load_csv(
            self.medication_file_path
        )

        self.analytics = RiskAnalyticsImpl(
            patients_df=self.patients_df,
            lab_results_df=self.lab_results_df,
            medications_df=self.medications_df
        )

    # =====================================================
    # Generic CSV Loader
    # =====================================================

    def _load_csv(
        self,
        file_path: str
    ) -> pd.DataFrame:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        df = pd.read_csv(path)

        if df.empty:
            raise ValueError(
                f"Dataset is empty: {file_path}"
            )

        return df

    # =====================================================
    # Dashboard KPIs
    # =====================================================

    def get_dashboard_kpis(self) -> Dict:

        return self.analytics.dashboard_kpis()

    # =====================================================
    # High Blood Pressure Rate
    # =====================================================

    def get_high_bp_rate(self) -> Dict:

        return self.analytics.high_bp_rate()

    # =====================================================
    # Obesity Rate
    # =====================================================

    def get_obesity_rate(self) -> Dict:

        return self.analytics.obesity_rate()

    # =====================================================
    # Tachycardia Rate
    # =====================================================

    def get_tachycardia_rate(self) -> Dict:

        return self.analytics.tachycardia_rate()

    # =====================================================
    # Abnormal Lab Rate
    # =====================================================

    def get_abnormal_lab_rate(self) -> Dict:

        return self.analytics.abnormal_lab_rate()

    # =====================================================
    # Medication Non-Adherence
    # =====================================================

    def get_medication_non_adherence_rate(
        self
    ) -> Dict:

        return self.analytics.medication_non_adherence_rate()

    # =====================================================
    # Charlson Risk Distribution
    # =====================================================

    def get_charlson_risk_distribution(
        self
    ) -> List[Dict]:

        return self.analytics.charlson_risk_distribution()

    # =====================================================
    # High Risk Patients
    # =====================================================

    def get_high_risk_patients(
        self
    ) -> List[Dict]:

        return self.analytics.high_risk_patients()

    # =====================================================
    # Risk Factor Summary
    # =====================================================

    def get_risk_factor_summary(
        self
    ) -> Dict:

        return self.analytics.risk_factor_summary()

    # =====================================================
    # Population Risk Score
    # =====================================================

    def get_population_risk_score(
        self
    ) -> Dict:

        return self.analytics.population_risk_score()