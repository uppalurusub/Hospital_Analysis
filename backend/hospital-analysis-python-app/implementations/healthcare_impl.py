from utils.data_loader import DataLoader
from utils.validator import DataValidator

from config.settings import (
    PATIENTS_FILE,
    DIAGNOSES_FILE,
    LAB_RESULTS_FILE,
    MEDICATIONS_FILE,
    OUTCOMES_FILE
)

class HealthcareAnalyticsImplementation:

    @staticmethod
    def load_all_datasets():

        patients = DataLoader.load_csv(PATIENTS_FILE)

        diagnoses = DataLoader.load_csv(DIAGNOSES_FILE)

        labs = DataLoader.load_csv(LAB_RESULTS_FILE)

        medications = DataLoader.load_csv(MEDICATIONS_FILE)

        outcomes = DataLoader.load_csv(OUTCOMES_FILE)

        return {
            "patients": patients,
            "diagnoses": diagnoses,
            "labs": labs,
            "medications": medications,
            "outcomes": outcomes
        }

    @staticmethod
    def validate_all():

        datasets = HealthcareAnalyticsImplementation.load_all_datasets()

        result = {}

        for name, df in datasets.items():

            result[name] = {
                "validation": DataValidator.validate_dataframe(df),
                "schema": DataValidator.schema_summary(df)
            }

        return result