"""
cost_service.py

Healthcare Cost Analytics Service Layer

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd

from implementations.cost_impl import (
    CostAnalyticsImpl
)


class CostAnalyticsService:

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

        self.analytics = CostAnalyticsImpl(
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
    # Average Cost
    # =====================================================

    def get_average_cost(
        self
    ) -> Dict:

        return self.analytics.average_cost()

    # =====================================================
    # Median Cost
    # =====================================================

    def get_median_cost(
        self
    ) -> Dict:

        return self.analytics.median_cost()

    # =====================================================
    # Total Cost
    # =====================================================

    def get_total_cost(
        self
    ) -> Dict:

        return self.analytics.total_cost()

    # =====================================================
    # Cost By Age Group
    # =====================================================

    def get_cost_by_age_group(
        self
    ) -> List[Dict]:

        return self.analytics.cost_by_age_group()

    # =====================================================
    # Cost By Gender
    # =====================================================

    def get_cost_by_gender(
        self
    ) -> List[Dict]:

        return self.analytics.cost_by_gender()

    # =====================================================
    # Cost By Disease
    # =====================================================

    def get_cost_by_disease(
        self
    ) -> List[Dict]:

        return self.analytics.cost_by_disease()

    # =====================================================
    # Cost By Charlson Risk
    # =====================================================

    def get_cost_by_charlson(
        self
    ) -> List[Dict]:

        return self.analytics.cost_by_charlson()

    # =====================================================
    # Cost By ICU
    # =====================================================

    def get_cost_by_icu(
        self
    ) -> Dict:

        return self.analytics.cost_by_icu()

    # =====================================================
    # LOS Cost Correlation
    # =====================================================

    def get_cost_los_analysis(
        self
    ) -> Dict:

        return self.analytics.cost_los_analysis()

    # =====================================================
    # High Cost Patients
    # =====================================================

    def get_high_cost_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.high_cost_patients(
            top_n=top_n
        )

    # =====================================================
    # Cost Summary
    # =====================================================

    def get_cost_summary(
        self
    ) -> Dict:

        return self.analytics.cost_summary()