import os
import matplotlib.pyplot as plt
from config import settings

#OUTPUT_DIR = "outputs/population_health"

OUTPUT_DIR = settings.OUTPUT_DIR

POPULATION_DIR = OUTPUT_DIR / "population"

CLINICAL_DIR = OUTPUT_DIR / "clinical"

CLINICAL_RISK_DIR = OUTPUT_DIR / "risks"

OUTCOMES_DIR = OUTPUT_DIR / "outcomes"

FINANCIAL_DIR = OUTPUT_DIR / "financial"

PREDICTION_DIR = OUTPUT_DIR / "prediction"

EXECUTIVE_DIR = OUTPUT_DIR / "executive"

DISEASES_DIR = OUTPUT_DIR / "diseases"

os.makedirs(
    OUTCOMES_DIR,
    exist_ok=True
)

os.makedirs(
    POPULATION_DIR,
    exist_ok=True
)

os.makedirs(
    CLINICAL_RISK_DIR,
    exist_ok=True
)

os.makedirs(
    CLINICAL_DIR,
    exist_ok=True
)

os.makedirs(
    FINANCIAL_DIR,
    exist_ok=True
)

os.makedirs(
    PREDICTION_DIR,
    exist_ok=True
)

os.makedirs(
    EXECUTIVE_DIR,
    exist_ok=True
)

os.makedirs(
    DISEASES_DIR,
    exist_ok=True
)

def save_chart_diseases(filename):

    filepath = f"{DISEASES_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_executive(filename):

    filepath = f"{EXECUTIVE_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_predictions(filename):

    filepath = f"{PREDICTION_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_financial(filename):

    filepath = f"{FINANCIAL_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_outcomes(filename):

    filepath = f"{OUTCOMES_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_clinical_risk(filename):

    filepath = f"{CLINICAL_RISK_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_population_health(filename):

    filepath = f"{POPULATION_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath

def save_chart_clinical(filename):

    filepath = f"{CLINICAL_DIR}/{filename}"

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return filepath