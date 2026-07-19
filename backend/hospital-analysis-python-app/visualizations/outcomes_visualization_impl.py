import io
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.chart_utils import save_chart_outcomes


class OutcomesVisualization:

    

    @staticmethod
    def generate_dashboard(
            outcomes_df,
            kpi_df,
            discharge_df
    ):

        

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(18, 12)
        )

        fig.suptitle(
            "Outcomes Analytics Dashboard",
            fontsize=20,
            fontweight="bold"
        )

        # ==================================
        # KPI Rates
        # ==================================

        sns.barplot(
            data=kpi_df,
            x="metric",
            y="value",
            ax=axes[0, 0]
        )

        axes[0, 0].set_title(
            "Outcome KPI Rates"
        )

        axes[0, 0].tick_params(
            axis="x",
            rotation=30
        )

        # ==================================
        # LOS Distribution
        # ==================================

        sns.histplot(
            data=outcomes_df,
            x="length_of_stay_days",
            kde=True,
            ax=axes[0, 1]
        )

        axes[0, 1].set_title(
            "Length of Stay Distribution"
        )

        # ==================================
        # Discharge Distribution
        # ==================================

        top_discharge = (
            discharge_df
            .sort_values(
                "count",
                ascending=False
            )
            .head(5)
        )

        sns.barplot(
            data=top_discharge,
            x="count",
            y="discharge_disposition",
            ax=axes[1, 0]
        )

        axes[1, 0].set_title(
            "Top Discharge Dispositions"
        )

        # ==================================
        # KPI Scorecard
        # ==================================

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

        save_chart_outcomes(
            "outcomes_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        return image_stream