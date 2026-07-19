# app/implementations/mlflow_inference_tracker.py

import uuid
import mlflow

from datetime import datetime

# =====================================================
# Configure MLflow
# =====================================================
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
#MLFLOW_TRACKING_URI = "file:./mlruns"

mlflow.set_tracking_uri(
    MLFLOW_TRACKING_URI
)

"""
mlflow.set_tracking_uri(
    "file:./mlruns"
)


mlflow.set_tracking_uri(
    "file:./mlruns"
)"""

mlflow.set_experiment(
    "Hospital_Analysis_Inference_Tracking"
)



# =====================================================
# Track Prediction Request
# =====================================================

def track_prediction_request(
    
    model_version="1.0"
):

    with mlflow.start_run(
        nested=True,
        #run_name=f"prediction_{request_data.patient_id}"
    ) as run:

        # -------------------------------------------------
        # MLflow Run Information
        # -------------------------------------------------

        run_id = run.info.run_id

        experiment_id = run.info.experiment_id

        request_id = str(uuid.uuid4())
        print(run_id)
        print(experiment_id)
        print(request_id)

        # -------------------------------------------------
        # Log Parameters
        # -------------------------------------------------

        mlflow.log_param(
            "request_id",
            request_id
        )

        

        mlflow.log_param(
            "model_version",
            model_version
        )

        """
        mlflow.log_param(
            "response",
            response_data
        )

        
        # -------------------------------------------------
        # Metrics
        # -------------------------------------------------

        mlflow.log_metric(
            "probability_score",
            float(probability_score)
        )

        mlflow.log_metric(
            "execution_time_ms",
            float(execution_time)
        )
        """
        # -------------------------------------------------
        # Tags
        # -------------------------------------------------

        mlflow.set_tag(
            "service",
            "Hospital Analysis"
        )

        mlflow.set_tag(
            "environment",
            "development"
        )

        """
        mlflow.set_tag(
            "patient_id",
            request_data.patient_id
        )

        mlflow.set_tag(
            "prediction",
            prediction_result
        )"""

        mlflow.set_tag(
            "timestamp",
            str(datetime.utcnow())
        )

        # -------------------------------------------------
        # Log Request JSON
        # -------------------------------------------------
        """
        mlflow.log_dict(
            request_data.dict(),
            "request.json"
        )"""

        # -------------------------------------------------
        # Log Response JSON
        # -------------------------------------------------

        """
        mlflow.log_dict(
            {
                "prediction": prediction_result,
                "probability_score": probability_score,
                "execution_time_ms": execution_time
            },
            "response.json"
        )"""

        # -------------------------------------------------
        # Print Tracking Details
        # -------------------------------------------------

        print("\n" + "=" * 60)

        print(
            "MLflow Tracking Completed Successfully"
        )

        print(f"Request ID : {request_id}")

        print(f"Run ID     : {run_id}")

        print(
            f"Run URL    : "
            f"http://127.0.0.1:5000/#/experiments/"
            f"{experiment_id}/runs/{run_id}"
        )

        print("=" * 60)