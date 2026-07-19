"""
medication_service.py

Medication Analytics Service Layer

Author: Healthcare Analytics Platform
"""

from pathlib import Path
from typing import Dict, List

import pandas as pd
import json
from implementations.medication_impl import (
    MedicationAnalyticsImpl
)
from implementations.mlflow_inference_tracker import (
    track_prediction_request
)


class MedicationAnalyticsService:

    def __init__(
        self,
        medication_file_path: str
    ):

        self.medication_file_path = medication_file_path

        self.medications_df = self._load_csv(
            self.medication_file_path
        )

        self.analytics = MedicationAnalyticsImpl(
            medications_df=self.medications_df
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

        # =================================================
        # ML Tracking
        # =================================================

        track_prediction_request(
            
            #response_data = json(self.analytics.dashboard_kpis())
        #    #execution_time=execution_time
        )
        return self.analytics.dashboard_kpis()

    # =====================================================
    # Overall Adherence Rate
    # =====================================================

    def get_adherence_rate(
        self
    ) -> Dict:

        return self.analytics.adherence_rate()

    # =====================================================
    # Non-Adherence Rate
    # =====================================================

    def get_non_adherence_rate(
        self
    ) -> Dict:

        return self.analytics.non_adherence_rate()

    # =====================================================
    # Top Medications
    # =====================================================

    def get_top_medications(
        self
    ) -> List[Dict]:

        return self.analytics.top_medications()

    # =====================================================
    # Adherence By Medication
    # =====================================================

    def get_adherence_by_medication(
        self
    ) -> List[Dict]:

        return self.analytics.adherence_by_medication()

    # =====================================================
    # Adherence By Indication
    # =====================================================

    def get_adherence_by_indication(
        self
    ) -> List[Dict]:

        return self.analytics.adherence_by_indication()

    # =====================================================
    # Generic Vs Brand
    # =====================================================

    def get_generic_vs_brand(
        self
    ) -> Dict:

        return self.analytics.generic_vs_brand()

    # =====================================================
    # High Risk Patients
    # =====================================================

    def get_high_risk_patients(
        self,
        top_n: int = 25
    ) -> List[Dict]:

        return self.analytics.high_risk_patients(
            top_n=top_n
        )

    # =====================================================
    # Medication Summary
    # =====================================================

    def get_medication_summary(
        self
    ) -> Dict:

        return self.analytics.medication_summary()