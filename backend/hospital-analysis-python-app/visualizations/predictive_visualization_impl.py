import io
import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from utils.chart_utils import save_chart_predictions

class PredictiveVisualization:

    

    @staticmethod
    def dashboard(metrics_df):

        

        fig, axes = plt.subplots(
            1,
            2,
            figsize=(16, 8)
        )

        sns.barplot(
            data=metrics_df,
            x="model",
            y="score",
            ax=axes[0]
        )

        axes[0].set_title(
            "Model Performance"
        )

        axes[0].tick_params(
            axis="x",
            rotation=25
        )

        axes[1].axis("off")

        scorecard = "\n".join(
            [
                f"{row.model}: {row.score}"
                for _, row in metrics_df.iterrows()
            ]
        )

        axes[1].text(
            0.05,
            0.4,
            scorecard,
            fontsize=14
        )

        plt.tight_layout()

        

        image_stream = io.BytesIO()

        plt.savefig(
            image_stream,
            format="png"
        )

        save_chart_predictions(
            "predictions_dashboard.png"
        )

        image_stream.seek(0)

        plt.close()

        return image_stream