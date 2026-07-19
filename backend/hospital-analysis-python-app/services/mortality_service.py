"""
mortality_service.py

Mortality Analytics Service Layer

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd

from implementations.mortality_impl import (
    MortalityAnalyticsImpl
)


class MortalityAnalyticsService:

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

        self.analytics = MortalityAnalyticsImpl(
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
    # Mortality Rate
    # =====================================================

    def get_mortality_rate(
        self
    ) -> Dict:

        return self.analytics.mortality_rate()

    # =====================================================
    # Mortality By Age Group
    # =====================================================

    def get_mortality_by_age_group(
        self
    ) -> List[Dict]:

        return self.analytics.mortality_by_age_group()

    # =====================================================
    # Mortality By Gender
    # =====================================================

    def get_mortality_by_gender(
        self
    ) -> List[Dict]:

        return self.analytics.mortality_by_gender()

    # =====================================================
    # Mortality By Charlson Risk
    # =====================================================

    def get_mortality_by_charlson(
        self
    ) -> List[Dict]:

        return self.analytics.mortality_by_charlson()

    # =====================================================
    # Mortality By ICU
    # =====================================================

    def get_mortality_by_icu(
        self
    ) -> Dict:

        return self.analytics.mortality_by_icu()

    # =====================================================
    # Mortality By Disease
    # =====================================================

    def get_mortality_by_disease(
        self
    ) -> List[Dict]:

        return self.analytics.mortality_by_disease()

    # =====================================================
    # High Mortality Risk Patients
    # =====================================================

    def get_high_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.high_risk_patients(
            top_n=top_n
        )

    # =====================================================
    # Risk Summary
    # =====================================================

    def get_risk_summary(
        self
    ) -> Dict:

        return self.analytics.risk_summary()