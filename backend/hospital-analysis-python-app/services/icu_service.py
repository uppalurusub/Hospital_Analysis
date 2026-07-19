"""
icu_service.py

ICU Analytics Service Layer

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

from implementations.icu_impl import (
    ICUAnalyticsImpl
)


class ICUAnalyticsService:

    def __init__(
        self,
        patient_file_path: str,
        outcome_file_path: str
    ):

        self.patient_file_path = patient_file_path
        self.outcome_file_path = outcome_file_path

        self.patients_df = self._load_csv(
            self.patient_file_path
        )

        self.outcomes_df = self._load_csv(
            self.outcome_file_path
        )

        self.analytics = ICUAnalyticsImpl(
            patients_df=self.patients_df,
            outcomes_df=self.outcomes_df
        )

    # =====================================================
    # CSV Loader
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

    def get_dashboard_kpis(
        self
    ) -> Dict:

        return self.analytics.dashboard_kpis()

    # =====================================================
    # ICU Admission Rate
    # =====================================================

    def get_icu_admission_rate(
        self
    ) -> Dict:

        return self.analytics.icu_admission_rate()

    # =====================================================
    # Average ICU Days
    # =====================================================

    def get_average_icu_days(
        self
    ) -> Dict:

        return self.analytics.average_icu_days()

    # =====================================================
    # ICU By Age Group
    # =====================================================

    def get_icu_by_age_group(
        self
    ) -> List[Dict]:

        return self.analytics.icu_by_age_group()

    # =====================================================
    # ICU By Gender
    # =====================================================

    def get_icu_by_gender(
        self
    ) -> List[Dict]:

        return self.analytics.icu_by_gender()

    # =====================================================
    # ICU By Charlson Risk
    # =====================================================

    def get_icu_by_charlson(
        self
    ) -> List[Dict]:

        return self.analytics.icu_by_charlson()

    # =====================================================
    # ICU By Disease
    # =====================================================

    def get_icu_by_disease(
        self
    ) -> List[Dict]:

        return self.analytics.icu_by_disease()

    # =====================================================
    # High ICU Risk Patients
    # =====================================================

    def get_high_icu_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.high_icu_risk_patients(
            top_n=top_n
        )

    # =====================================================
    # ICU Risk Summary
    # =====================================================

    def get_icu_risk_summary(
        self
    ) -> Dict:

        return self.analytics.icu_risk_summary()