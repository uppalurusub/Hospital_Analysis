"""
los_service.py

Length of Stay (LOS) Analytics Service Layer

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd

from implementations.los_impl import (
    LOSAnalyticsImpl
)


class LOSAnalyticsService:

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

        self.analytics = LOSAnalyticsImpl(
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
    # Average LOS
    # =====================================================

    def get_average_los(
        self
    ) -> Dict:

        return self.analytics.average_los()

    # =====================================================
    # Median LOS
    # =====================================================

    def get_median_los(
        self
    ) -> Dict:

        return self.analytics.median_los()

    # =====================================================
    # LOS By Age Group
    # =====================================================

    def get_los_by_age_group(
        self
    ) -> List[Dict]:

        return self.analytics.los_by_age_group()

    # =====================================================
    # LOS By Gender
    # =====================================================

    def get_los_by_gender(
        self
    ) -> List[Dict]:

        return self.analytics.los_by_gender()

    # =====================================================
    # LOS By Disease
    # =====================================================

    def get_los_by_disease(
        self
    ) -> List[Dict]:

        return self.analytics.los_by_disease()

    # =====================================================
    # LOS By Charlson Risk
    # =====================================================

    def get_los_by_charlson(
        self
    ) -> List[Dict]:

        return self.analytics.los_by_charlson()

    # =====================================================
    # LOS By ICU
    # =====================================================

    def get_los_by_icu(
        self
    ) -> Dict:

        return self.analytics.los_by_icu()

    # =====================================================
    # Long Stay Patients
    # =====================================================

    def get_long_stay_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.long_stay_patients(
            top_n=top_n
        )

    # =====================================================
    # LOS Summary
    # =====================================================

    def get_los_summary(
        self
    ) -> Dict:

        return self.analytics.los_summary()