
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import io
import seaborn as sns
import matplotlib.pyplot as plt

from utils.chart_utils import save_chart_population_health
from implementations.healthcare_impl import HealthcareAnalyticsImplementation

import pandas as pd

class PopulationAnalyticsVisualization:

    datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
    )

    df = datasets["patients"]

    @staticmethod
    def age_distribution(df):

        plt.figure(figsize=(10,6))

        sns.histplot(
            data=df,
            x="age",
            bins=20,
            kde=True
        )

        plt.title(
            "Age Distribution"
        )

        return save_chart_population_health(
            "age_distribution.png"
        )

    @staticmethod
    def gender_mix(df):

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=df,
            x="sex"
        )

        plt.title(
            "Gender Mix"
        )

        return save_chart_population_health(
            "gender_mix.png"
        )

    @staticmethod
    def bmi_categories(df):

        temp = df.copy()

        temp["bmi_category"] = pd.cut(
            temp["bmi"],
            bins=[
                0,
                18.5,
                25,
                30,
                100
            ],
            labels=[
                "Underweight",
                "Normal",
                "Overweight",
                "Obese"
            ]
        )

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=temp,
            x="bmi_category"
        )

        plt.title(
            "BMI Categories"
        )

        return save_chart_population_health(
            "bmi_categories.png"
        )

    @staticmethod
    def smoking_rate(df):

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=df,
            x="smoking_status"
        )

        plt.title(
            "Smoking Status"
        )

        return save_chart_population_health(
            "smoking_rate.png"
        )

    @staticmethod
    def alcohol_usage(df):

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=df,
            x="alcohol_use"
        )

        plt.title(
            "Alcohol Usage"
        )

        return save_chart_population_health(
            "alcohol_usage.png"
        )

    @staticmethod
    def exercise_compliance(df):

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=df,
            x="exercise_level"
        )

        plt.title(
            "Exercise Compliance"
        )

        return save_chart_population_health(
            "exercise_compliance.png"
        )

    @staticmethod
    def charlson_distribution(df):

        plt.figure(figsize=(8,5))

        sns.histplot(
            data=df,
            x="charlson_index",
            bins=10,
            kde=True
        )

        plt.title(
            "Charlson Score Distribution"
        )

        return save_chart_population_health(
            "charlson_distribution.png"
        )
    
    @staticmethod
    def dashboard(df):

        fig, axes = plt.subplots(
            nrows=4,
            ncols=2,
            figsize=(20, 18)
        )

        fig.suptitle(
            "Population Health Analytics Dashboard",
            fontsize=20,
            fontweight="bold"
        )

        # ----------------------------
        # Age Distribution
        # ----------------------------

        sns.histplot(
            data=df,
            x="age",
            kde=True,
            ax=axes[0, 0]
        )

        axes[0, 0].set_title(
            "Age Distribution"
        )

       

        # ----------------------------
        # Gender Mix
        # ----------------------------

        sns.countplot(
            data=df,
            x="sex",
            ax=axes[0, 1]
        )

        axes[0, 1].set_title(
            "Gender Mix"
        )

        # ----------------------------
        # BMI Categories
        # ----------------------------

        bmi_df = df.copy()

        bmi_df["bmi_category"] = pd.cut(
            bmi_df["bmi"],
            bins=[0, 18.5, 25, 30, 100],
            labels=[
                "Underweight",
                "Normal",
                "Overweight",
                "Obese"
            ]
        )

        sns.countplot(
            data=bmi_df,
            x="bmi_category",
            ax=axes[1, 0]
        )

        axes[1, 0].set_title(
            "BMI Categories"
        )

        # ----------------------------
        # Smoking
        # ----------------------------

        sns.countplot(
            data=df,
            x="smoking_status",
            ax=axes[1, 1]
        )

        axes[1, 1].set_title(
            "Smoking Status"
        )

        # ----------------------------
        # Alcohol
        # ----------------------------

        sns.countplot(
            data=df,
            x="alcohol_use",
            ax=axes[2, 0]
        )

        axes[2, 0].set_title(
            "Alcohol Usage"
        )

        # ----------------------------
        # Exercise
        # ----------------------------

        sns.countplot(
            data=df,
            x="exercise_level",
            ax=axes[2, 1]
        )

        axes[2, 1].set_title(
            "Exercise Compliance"
        )

        # ----------------------------
        # Charlson Score
        # ----------------------------

        sns.histplot(
            data=df,
            x="charlson_index",
            kde=True,
            ax=axes[3, 0]
        )

        axes[3, 0].set_title(
            "Charlson Score Distribution"
        )

        # ----------------------------
        # KPI Scorecard
        # ----------------------------

        axes[3, 1].axis("off")

        total_patients = df["patient_id"].nunique()

        avg_age = round(df["age"].mean(), 2)

        avg_bmi = round(df["bmi"].mean(), 2)

        avg_charlson = round(
            df["charlson_index"].mean(),
            2
        )

        kpi_text = f"""
        Total Patients : {total_patients}

        Average Age : {avg_age}

        Average BMI : {avg_bmi}

        Average Charlson : {avg_charlson}
        """

        axes[3, 1].text(
            0.1,
            0.5,
            kpi_text,
            fontsize=14
        )

        plt.tight_layout()

        image_stream = io.BytesIO()

        plt.savefig(
            image_stream,
            format="png",
            bbox_inches="tight",
            dpi=300
        )

        save_chart_population_health(
            "population_health_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        

        return image_stream