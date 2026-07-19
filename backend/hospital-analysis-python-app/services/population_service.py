"""
population_service.py

Service Layer
-------------
Acts as a bridge between Router and Implementation.

Responsibilities:
1. Load patient dataset
2. Validate data
3. Invoke implementation methods
4. Handle exceptions
5. Return  results

Author: Healthcare  Platform
"""

from pathlib import Path
from typing import Dict, List
import pandas as pd

from implementations.population_impl import (
    PopulationAnalyticsImpl
)



class PopulationAnalyticsService:

    @staticmethod
    def get_population_health_kpis():

        return (
            PopulationAnalyticsImpl
            .get_population_health_kpis()
        )

    

    # =====================================================
    # Population Overview
    # =====================================================
    @staticmethod
    def get_population_summary():

        return PopulationAnalyticsImpl.population_summary()

    # =====================================================
    # Age Distribution
    # =====================================================
    @staticmethod
    def get_age_distribution():

        return PopulationAnalyticsImpl.age_distribution()

    # =====================================================
    # Gender Distribution
    # =====================================================
    @staticmethod
    def get_gender_distribution():

        return PopulationAnalyticsImpl.gender_distribution()

    # =====================================================
    # Smoking Analysis
    # =====================================================
    @staticmethod
    def get_smoking_analysis():

        return PopulationAnalyticsImpl.smoking_analysis()

    # =====================================================
    # Alcohol Analysis
    # =====================================================
    @staticmethod
    def get_alcohol_analysis():

        return PopulationAnalyticsImpl.alcohol_analysis()

    # =====================================================
    # Exercise Analysis
    # =====================================================
    @staticmethod
    def get_exercise_analysis():

        return PopulationAnalyticsImpl.exercise_analysis()

    # =====================================================
    # Obesity Analysis
    # =====================================================
    @staticmethod
    def get_obesity_analysis():

        return PopulationAnalyticsImpl.obesity_analysis()

    # =====================================================
    # Hypertension Analysis
    # =====================================================
    @staticmethod
    def get_hypertension_analysis():

        return PopulationAnalyticsImpl.hypertension_analysis()

    # =====================================================
    # Diabetes Analysis
    # =====================================================
    @staticmethod
    def get_diabetes_analysis():

        return PopulationAnalyticsImpl.diabetes_analysis()

    # =====================================================
    # Top Risk Factors
    # =====================================================
    @staticmethod
    def get_top_risk_factors():

        return PopulationAnalyticsImpl.top_risk_factors()

    # =====================================================
    # Dashboard 
    # =====================================================
    
    @staticmethod
    def dashboard():
        return PopulationAnalyticsImpl.dashboard()