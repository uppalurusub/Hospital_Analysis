import io
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from utils.chart_utils import save_chart_financial


class FinancialVisualization:

    
    @staticmethod
    def generate_dashboard(
            outcomes_df,
            drg_df,
            diagnosis_df,
            kpi_df
    ):

        

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(20, 12)
        )

        fig.suptitle(
            "Financial Analytics Dashboard",
            fontsize=20,
            fontweight="bold"
        )

        # ==========================
        # Cost Per DRG
        # ==========================

        sns.barplot(
            data=drg_df.head(10),
            x="avg_cost",
            y="primary_drg",
            ax=axes[0, 0]
        )

        axes[0, 0].set_title(
            "Top DRGs by Cost"
        )

        # ==========================
        # Cost Per Diagnosis
        # ==========================

        sns.barplot(
            data=diagnosis_df.head(10),
            x="avg_cost",
            y="primary_diagnosis",
            ax=axes[0, 1]
        )

        axes[0, 1].set_title(
            "Top Diagnoses by Cost"
        )

        # ==========================
        # Cost Distribution
        # ==========================

        sns.histplot(
            outcomes_df["total_charges_usd"],
            kde=True,
            ax=axes[1, 0]
        )

        axes[1, 0].set_title(
            "Cost Distribution"
        )

        # ==========================
        # KPI Scorecard
        # ==========================

        axes[1, 1].axis("off")

        scorecard = "\n".join(
            [
                f"{row.metric}: {row.value}"
                for _, row in kpi_df.iterrows()
            ]
        )

        axes[1, 1].text(
            0.05,
            0.4,
            scorecard,
            fontsize=14
        )

        plt.tight_layout()

        

        image_stream = io.BytesIO()

        plt.savefig(
            image_stream,
            format="png",
            dpi=300,
            bbox_inches="tight"
        )

        save_chart_financial(
            "financial_dashboard.png"
            )

        image_stream.seek(0)

        plt.close()

        return image_stream