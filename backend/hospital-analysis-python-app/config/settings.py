from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
print(DATA_DIR)
print(OUTPUT_DIR)

PATIENTS_FILE = DATA_DIR / "patients.csv"
DIAGNOSES_FILE = DATA_DIR / "diagnoses.csv"
LAB_RESULTS_FILE = DATA_DIR / "lab_results.csv"
MEDICATIONS_FILE = DATA_DIR / "medications.csv"
OUTCOMES_FILE = DATA_DIR / "outcomes.csv"


