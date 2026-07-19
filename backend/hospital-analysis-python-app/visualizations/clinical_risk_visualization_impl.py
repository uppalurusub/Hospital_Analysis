import io
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from utils.chart_utils import save_chart_clinical_risk

class ClinicalRiskVisualization:

    #OUTPUT_DIR = "outputs/clinical_risk"

    @staticmethod
    def generate_dashboard(kpi_df):

        

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(18, 12)
        )

        fig.suptitle(
            "Clinical Risk Analytics Dashboard",
            fontsize=20,
            fontweight="bold"
        )

        # Risk Rate Bar Chart

        sns.barplot(
            data=kpi_df,
            x="risk_metric",
            y="rate",
            ax=axes[0, 0]
        )

        axes[0, 0].set_title(
            "Clinical Risk Rates (%)"
        )

        axes[0, 0].tick_params(
            axis="x",
            rotation=30
        )

        # Horizontal Ranking

        sns.barplot(
            data=kpi_df.sort_values(
                "rate",
                ascending=False
            ),
            x="rate",
            y="risk_metric",
            ax=axes[0, 1]
        )

        axes[0, 1].set_title(
            "Risk Ranking"
        )

        # Top Risks Pie

        top_df = (
            kpi_df
            .sort_values(
                "rate",
                ascending=False
            )
            .head(5)
        )

        axes[1, 0].pie(
            top_df["rate"],
            labels=top_df["risk_metric"],
            autopct="%1.1f%%",
            startangle=90
        )

        axes[1, 0].set_title(
            "Risk Contribution"
        )

        # KPI Scorecard

        axes[1, 1].axis("off")

        kpi_text = "\n".join(
            [
                f"{row['risk_metric']}: "
                f"{row['rate']}%"
                for _, row in kpi_df.iterrows()
            ]
        )

        axes[1, 1].text(
            0.05,
            0.5,
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

        save_chart_clinical_risk(
            "clinical_risk_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        return image_stream