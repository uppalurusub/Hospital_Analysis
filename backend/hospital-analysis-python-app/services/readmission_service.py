"""
readmission_service.py

Readmission Analytics Service Layer

Responsibilities
----------------
1. Load datasets
2. Validate datasets
3. Invoke implementation layer
4. Return JSON serializable responses

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd

from implementations.readmission_impl import (
    ReadmissionAnalyticsImpl
)


class ReadmissionAnalyticsService:

    def __init__(
        self,
        patient_file_path: str,
        outcome_file_path: str,
        medication_file_path: str = None
    ):

        self.patient_file_path = patient_file_path
        self.outcome_file_path = outcome_file_path
        self.medication_file_path = medication_file_path

        self.patients_df = self._load_csv(
            self.patient_file_path
        )

        self.outcomes_df = self._load_csv(
            self.outcome_file_path
        )

        if medication_file_path:
            self.medications_df = self._load_csv(
                self.medication_file_path
            )
        else:
            self.medications_df = pd.DataFrame()

        self.analytics = ReadmissionAnalyticsImpl(
            patients_df=self.patients_df,
            outcomes_df=self.outcomes_df,
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
    # Readmission Rate
    # =====================================================

    def get_readmission_rate(self) -> Dict:

        return self.analytics.readmission_rate()

    # =====================================================
    # Average Days To Readmission
    # =====================================================

    def get_average_days_to_readmission(
        self
    ) -> Dict:

        return self.analytics.average_days_to_readmission()

    # =====================================================
    # Readmission By Age Group
    # =====================================================

    def get_readmission_by_age_group(
        self
    ) -> List[Dict]:

        return self.analytics.readmission_by_age_group()

    # =====================================================
    # Readmission By Charlson Index
    # =====================================================

    def get_readmission_by_charlson(
        self
    ) -> List[Dict]:

        return self.analytics.readmission_by_charlson()

    # =====================================================
    # Readmission By Medication Adherence
    # =====================================================

    def get_readmission_by_adherence(
        self
    ) -> Dict:

        return self.analytics.readmission_by_adherence()

    # =====================================================
    # High Readmission Risk Patients
    # =====================================================

    def get_high_readmission_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.high_readmission_risk_patients(
            top_n=top_n
        )

    # =====================================================
    # Readmission Risk Summary
    # =====================================================

    def get_readmission_risk_summary(
        self
    ) -> Dict:

        return self.analytics.readmission_risk_summary()