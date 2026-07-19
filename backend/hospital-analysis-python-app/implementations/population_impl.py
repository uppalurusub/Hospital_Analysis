"""
population_impl.py

Implementation Layer
--------------------
Contains actual business logic for Population Health Analytics.

Responsibilities:
1. Population Demographics
2. Risk Factor Analysis
3. Disease Burden Analysis
4. Age Segmentation
5. Gender Distribution
6. Population Summary KPIs

Author: Healthcare Analytics Platform
"""

from typing import Dict, List
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)



from visualizations.population_visualization_impl import (
    PopulationAnalyticsVisualization
)


class PopulationAnalyticsImpl:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        return (
            PopulationAnalyticsVisualization
            .dashboard(
                patients_df
            )
        )
    
    

    

    # ==========================================================
    # Population Overview
    # ==========================================================
    

    @staticmethod
    def population_summary():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]


        total_patients = patients_df["patient_id"].nunique()

        avg_age = round(patients_df["age"].mean(), 2)

        avg_bmi = round(patients_df["bmi"].mean(), 2)

        male_count = len(patients_df[patients_df["sex"] == "M"])
        female_count = len(patients_df[patients_df["sex"] == "F"])

        return {
            "total_patients": total_patients,
            "average_age": avg_age,
            "average_bmi": avg_bmi,
            "male_patients": male_count,
            "female_patients": female_count
        }

    # ==========================================================
    # Age Distribution
    # ==========================================================

    @staticmethod
    def age_distribution():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]


        bins = [0, 18, 35, 50, 65, 80, 120]

        labels = [
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "66-80",
            "80+"
        ]

        patients_df["age_group"] = pd.cut(
            patients_df["age"],
            bins=bins,
            labels=labels
        )

        result = (
            patients_df["age_group"]
            .value_counts()
            .reset_index()
        )

        result.columns = [
            "age_group",
            "patient_count"
        ]

        #eturn result
        return result.to_dict(
            orient="records"
        )

    # ==========================================================
    # Gender Distribution
    # ==========================================================
    @staticmethod
    def gender_distribution():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        result = (
            patients_df["sex"]
            .value_counts()
            .reset_index()
        )

        result.columns = [
            "gender",
            "patient_count"
        ]

        #return result
        return result.to_dict(
            orient="records"
        )

    # ==========================================================
    # Smoking Analysis
    # ==========================================================
    @staticmethod
    def smoking_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        smokers = len(
            patients_df[
                patients_df["smoking_status"]
                .str.lower()
                .isin(["current", "former"])
            ]
        )

        total = len(patients_df)

        smoking_rate = round(
            (smokers / total) * 100,
            2
        )

        return {
            "smokers": smokers,
            "total_patients": total,
            "smoking_rate_pct": smoking_rate
        }

    # ==========================================================
    # Alcohol Usage Analysis
    # ==========================================================
    @staticmethod
    def alcohol_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        alcohol_users = len(
            patients_df[
                patients_df["alcohol_use"]
                .str.lower()
                .isin(["light", "moderate","heavy"])
            ]
        )

        total = len(patients_df)

        alcohol_rate = round(
            (alcohol_users / total) * 100,
            2
        )

        return {
            "alcohol_users": alcohol_users,
            "alcohol_rate_pct": alcohol_rate
        }

    # ==========================================================
    # Exercise Analysis
    # ==========================================================
    @staticmethod
    def exercise_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        result = (
            patients_df["exercise_level"]
            .value_counts()
            .reset_index()
        )

        result.columns = [
            "exercise_level",
            "patient_count"
        ]

        return result.to_dict(
            orient="records"
        )

    # ==========================================================
    # Obesity Analysis
    # ==========================================================
    @staticmethod
    def obesity_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        obese = len(
            patients_df[
                patients_df["bmi"] >= 30
            ]
        )

        total = len(patients_df)

        obesity_rate = round(
            (obese / total) * 100,
            2
        )

        return {
            "obese_patients": obese,
            "obesity_rate_pct": obesity_rate
        }

    # ==========================================================
    # Hypertension Analysis
    # ==========================================================
    @staticmethod
    def hypertension_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        hypertensive = len(
            patients_df[
                patients_df["dx_hypertension"] == 1
            ]
        )

        total = len(patients_df)

        prevalence = round(
            (hypertensive / total) * 100,
            2
        )

        return {
            "hypertension_patients": hypertensive,
            "hypertension_prevalence_pct": prevalence
        }

    # ==========================================================
    # Diabetes Analysis
    # ==========================================================
    @staticmethod
    def diabetes_analysis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        diabetic = len(
            patients_df[
                (patients_df["dx_type1_diabetes"] == 1)
                |
                (patients_df["dx_type2_diabetes"] == 1)
            ]
        )

        total = len(patients_df)

        prevalence = round(
            (diabetic / total) * 100,
            2
        )

        return {
            "diabetes_patients": diabetic,
            "diabetes_prevalence_pct": prevalence
        }

    # ==========================================================
    # Top Risk Factors
    # ==========================================================
    @staticmethod
    def top_risk_factors():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        total = len(patients_df)

        metrics = {
            "Smoking":
                len(
                    patients_df[
                        patients_df["smoking_status"]
                        .str.lower()
                        .isin(["current", "former"])
                    ]
                ),

            "Obesity":
                len(
                    patients_df[
                        patients_df["bmi"] >= 30
                    ]
                ),

            "Hypertension":
                len(
                    patients_df[
                        patients_df["dx_hypertension"] == 1
                    ]
                ),

            "Type2 Diabetes":
                len(
                    patients_df[
                        patients_df["dx_type2_diabetes"] == 1
                    ]
                )
        }

        output = []

        for risk_factor, count in metrics.items():

            output.append({
                "risk_factor": risk_factor,
                "patient_count": count,
                "prevalence_pct": round(
                    count * 100 / total,
                    2
                )
            })

        return sorted(
            output,
            key=lambda x: x["prevalence_pct"],
            reverse=True
        )

    # ==========================================================
    # Population Dashboard KPI
    # ==========================================================
    @staticmethod
    def get_population_health_kpis():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        total_patients = int(
            patients_df["patient_id"].nunique()
        )

        return {

            "total_patients":
                total_patients,

            "age_statistics":
                PopulationAnalyticsImpl
                .calculate_age_statistics(
                    patients_df
                ),

            "age_distribution":
                PopulationAnalyticsImpl
                .calculate_age_distribution(
                    patients_df
                ),

            "gender_mix":
                PopulationAnalyticsImpl
                .calculate_gender_mix(
                    patients_df
                ),

            "bmi_categories":
                PopulationAnalyticsImpl
                .calculate_bmi_categories(
                    patients_df
                ),

            "smoking_rate":
                PopulationAnalyticsImpl
                .calculate_smoking_rate(
                    patients_df
                ),

            "alcohol_usage_rate":
                PopulationAnalyticsImpl
                .calculate_alcohol_usage(
                    patients_df
                ),

            "exercise_compliance":
                PopulationAnalyticsImpl
                .calculate_exercise_compliance(
                    patients_df
                ),

            "charlson_distribution":
                PopulationAnalyticsImpl
                .calculate_charlson_distribution(
                    patients_df
                )
        }

    