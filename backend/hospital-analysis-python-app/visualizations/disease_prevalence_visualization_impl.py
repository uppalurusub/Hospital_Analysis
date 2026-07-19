import os
import io
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from utils.chart_utils import save_chart_diseases

from config import settings



class DiseasePrevalenceVisualization:

    

    @staticmethod
    def generate_dashboard(
            prevalence_df,
            total_patients,
            multimorbidity_rate
    ):

        

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(18, 12)
        )

        fig.suptitle(
            "Disease Prevalence Analytics Dashboard",
            fontsize=20,
            fontweight="bold"
        )

        # =====================================
        # Disease Prevalence
        # =====================================

        sns.barplot(
            data=prevalence_df,
            x="prevalence_pct",
            y="disease",
            ax=axes[0, 0]
        )

        axes[0, 0].set_title(
            "Disease Prevalence (%)"
        )

        # =====================================
        # Patient Count
        # =====================================

        sns.barplot(
            data=prevalence_df,
            x="patient_count",
            y="disease",
            ax=axes[0, 1]
        )

        axes[0, 1].set_title(
            "Affected Patients"
        )

        # =====================================
        # Pie Chart
        # =====================================

        # =====================================
        # Top 5 Disease Burden Pie Chart
        # =====================================

        top_5_df = (
            prevalence_df
            .sort_values(
                by="patient_count",
                ascending=False
            )
            .head(5)
        )

        others_count = (
            prevalence_df["patient_count"].sum()
            - top_5_df["patient_count"].sum()
        )

        if others_count > 0:

            others_row = pd.DataFrame({
                "disease": ["Others"],
                "patient_count": [others_count]
            })

            top_5_df = pd.concat(
                [top_5_df, others_row],
                ignore_index=True
            )

        axes[1, 0].pie(
            top_5_df["patient_count"],
            labels=top_5_df["disease"],
            autopct="%1.1f%%",
            startangle=90
        )

        axes[1, 0].set_title(
            "Top 5 Disease Burden"
        )

        # =====================================
        # KPI Scorecard
        # =====================================

        axes[1, 1].axis("off")
        print(prevalence_df.head())

        print(prevalence_df.columns)

        print(prevalence_df.shape)
        
        kpi_text = f"""
Disease Prevalence KPIs

Total Patients: {total_patients}

Hypertension:
{prevalence_df.loc[
 prevalence_df.disease=='dx_hypertension',
 'prevalence_pct'
].iloc[0]}%

Diabetes:
{prevalence_df.loc[
 prevalence_df.disease=='dx_type2_diabetes',
 'prevalence_pct'
].iloc[0]}%

Multi-Morbidity Rate:
{multimorbidity_rate}%
        """

        axes[1, 1].text(
            0.05,
            0.4,
            kpi_text,
            fontsize=14
        )

        plt.tight_layout()

        

        

        # Stream Dashboard

        image_stream = io.BytesIO()

        plt.savefig(
            image_stream,
            format="png",
            dpi=300,
            bbox_inches="tight"
        )

        save_chart_diseases(
            "diseases_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        return image_stream

        