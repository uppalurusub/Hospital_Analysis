import io
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from utils.chart_utils import save_chart_executive

class ExecutiveDashboardVisualization:

    

    @staticmethod
    def generate_dashboard(
            executive_metrics
    ):

        

        fig = plt.figure(
            figsize=(24, 16)
        )

        fig.suptitle(
            "Healthcare Executive Dashboard",
            fontsize=24,
            fontweight="bold"
        )

        # Population

        plt.subplot(3, 2, 1)

        plt.axis("off")

        plt.title(
            "Population Overview"
        )

        plt.text(
            0,
            0.8,
            executive_metrics[
                "population_text"
            ],
            fontsize=12
        )

        # Disease

        plt.subplot(3, 2, 2)

        plt.axis("off")

        plt.title(
            "Disease Burden"
        )

        plt.text(
            0,
            0.8,
            executive_metrics[
                "disease_text"
            ],
            fontsize=12
        )

        # Clinical

        plt.subplot(3, 2, 3)

        plt.axis("off")

        plt.title(
            "Clinical Quality"
        )

        plt.text(
            0,
            0.8,
            executive_metrics[
                "clinical_text"
            ],
            fontsize=12
        )

        # Outcomes

        plt.subplot(3, 2, 4)

        plt.axis("off")

        plt.title(
            "Operational Performance"
        )

        plt.text(
            0,
            0.8,
            executive_metrics[
                "outcomes_text"
            ],
            fontsize=12
        )

        # Financial

        plt.subplot(3, 2, 5)

        plt.axis("off")

        plt.title(
            "Financial Performance"
        )

        plt.text(
            0,
            0.8,
            executive_metrics[
                "financial_text"
            ],
            fontsize=12
        )

        

        

        plt.tight_layout()

        

        image_stream = io.BytesIO()

        plt.savefig(
            image_stream,
            format="png",
            dpi=300,
            bbox_inches="tight"
        )

        save_chart_executive(
            "executive_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        return image_stream