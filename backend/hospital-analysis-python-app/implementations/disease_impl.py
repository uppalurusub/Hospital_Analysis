import pandas as pd

from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from visualizations.disease_prevalence_visualization_impl import (
    DiseasePrevalenceVisualization
)

datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

patients_df = datasets["patients"]


class DiseaseImplementation: 

    DISEASE_MAPPING = {
            "Hypertension": "dx_hypertension",
            "Type 2 Diabetes": "dx_type2_diabetes",
            "Type 1 Diabetes": "dx_type1_diabetes",
            "Hyperlipidemia": "dx_hyperlipidemia",
            "Obesity": "dx_obesity",
            "Coronary Artery Disease": "dx_coronary_artery_disease",
            "Heart Failure": "dx_heart_failure",
            "Atrial Fibrillation": "dx_atrial_fibrillation",
            "Chronic Kidney Disease": "dx_chronic_kidney_disease",
            "COPD": "dx_copd",
            "Asthma": "dx_asthma",
            "Depression": "dx_depression",
            "Anxiety": "dx_anxiety",
            "Hypothyroidism": "dx_hypothyroidism",
            "Osteoarthritis": "dx_osteoarthritis"
    }

    # =====================================================
    # Individual Disease APIs
    # =====================================================

    
    @staticmethod
    def _calculate_prevalence(
        disease_name: str,
        column_name: str
    ):

        total_patients = int(len(patients_df))

        disease_patients = int(
            patients_df[column_name].fillna(0).sum()
        )

        prevalence = round(
            (disease_patients / total_patients) * 100,
            2
        )

        return {
            "disease": disease_name,
            "patient_count": disease_patients,
            "total_patients": total_patients,
            "prevalence_pct": float(prevalence)
        }

    def hypertension_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Hypertension",
            "dx_hypertension"
        )

    def type2_diabetes_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Type 2 Diabetes",
            "dx_type2_diabetes"
        )

    def ckd_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Chronic Kidney Disease",
            "dx_chronic_kidney_disease"
        )

    def cad_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Coronary Artery Disease",
            "dx_coronary_artery_disease"
        )

    def heart_failure_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Heart Failure",
            "dx_heart_failure"
        )

    def copd_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "COPD",
            "dx_copd"
        )

    def asthma_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Asthma",
            "dx_asthma"
        )

    def depression_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Depression",
            "dx_depression"
        )

    def anxiety_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Anxiety",
            "dx_anxiety"
        )

    def obesity_prevalence():
        return DiseaseImplementation._calculate_prevalence(
            "Obesity",
            "dx_obesity"
        )

    # =====================================================
    # Top Diseases
    # =====================================================
    @staticmethod
    def top_diseases():

        

        total_patients = int(len(patients_df))

        disease_stats = []

        for disease_name, column_name in DiseaseImplementation.DISEASE_MAPPING.items():

            patient_count = int(
                patients_df[column_name].fillna(0).sum()
            )

            prevalence = round(
                (patient_count / total_patients) * 100,
                2
            )

            disease_stats.append({
                "disease": disease_name,
                "patient_count": patient_count,
                "prevalence_pct": float(prevalence)
            })

        disease_stats = sorted(
            disease_stats,
            key=lambda x: x["patient_count"],
            reverse=True
        )

        return disease_stats

    # =====================================================
    # Comorbidity Analysis
    # =====================================================
    @staticmethod
    def comorbidity_analysis():

        disease_cols = list(
            DiseaseImplementation.DISEASE_MAPPING.values()
        )

        patients_df["disease_count"] = (
            patients_df[disease_cols]
            .fillna(0)
            .sum(axis=1)
        )

        result = (
            patients_df["disease_count"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        result.columns = [
            "number_of_diseases",
            "patient_count"
        ]

        result["number_of_diseases"] = (
            result["number_of_diseases"]
            .astype(int)
        )

        result["patient_count"] = (
            result["patient_count"]
            .astype(int)
        )

        return result.to_dict(
            orient="records"
        )

    # =====================================================
    # Chronic Disease Burden
    # =====================================================
    @staticmethod
    def chronic_disease_burden():

        disease_cols = list(
            DiseaseImplementation.DISEASE_MAPPING.values()
        )

        disease_count_per_patient = (
            patients_df[disease_cols]
            .fillna(0)
            .sum(axis=1)
        )

        avg_disease_count = round(
            float(
                disease_count_per_patient.mean()
            ),
            2
        )

        max_disease_count = int(
            disease_count_per_patient.max()
        )

        patients_with_3_plus = int(
            (
                disease_count_per_patient >= 3
            ).sum()
        )

        total_patients = int(len(patients_df))

        multimorbidity_rate = round(
            (
                patients_with_3_plus /
                total_patients
            ) * 100,
            2
        )

        return {
            "average_diseases_per_patient":
                avg_disease_count,

            "max_diseases_per_patient":
                max_disease_count,

            "patients_with_3_or_more_conditions":
                patients_with_3_plus,

            "multimorbidity_rate_pct":
                float(multimorbidity_rate)
        }

    
    @staticmethod
    def generate_dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]

        total_patients = int(
            patients_df["patient_id"]
            .nunique()
        )

        disease_results = []

        for column, disease_name in (
                DiseaseImplementation
                .DISEASE_MAPPING.items()
        ):
            print(column)
            print(disease_name)
            patient_count = int(
                #patients_df[column]
                patients_df[disease_name]
                .fillna(0)
                .sum()
            )

            prevalence_pct = round(
                (
                    patient_count /
                    total_patients
                ) * 100,
                2
            )

            disease_results.append(
                {
                    "disease":
                        disease_name,

                    "patient_count":
                        patient_count,

                    "prevalence_pct":
                        prevalence_pct
                }
            )

        prevalence_df = pd.DataFrame(
            disease_results
        )

        prevalence_df = (
            prevalence_df
            .sort_values(
                "prevalence_pct",
                ascending=False
            )
        )

        DISEASE_MAPPING = list(
            DiseaseImplementation
            .DISEASE_MAPPING.keys()
        )

        disease_columns = list(DiseaseImplementation.DISEASE_MAPPING.values())

        patients_df[
            "disease_count"
        ] = (
            patients_df[disease_columns]
            .fillna(0)
            .sum(axis=1)
        )

        multimorbidity_rate = round(
            (
                (
                    patients_df[
                        "disease_count"
                    ] >= 2
                ).sum()
                / total_patients
            ) * 100,
            2
        )

        return (
            DiseasePrevalenceVisualization
            .generate_dashboard(
                prevalence_df,
                total_patients,
                multimorbidity_rate
            )
        )        