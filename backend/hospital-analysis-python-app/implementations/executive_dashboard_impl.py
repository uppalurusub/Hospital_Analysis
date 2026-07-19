from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

from visualizations.executive_dashboard_visualization_impl import (
    ExecutiveDashboardVisualization
)


class ExecutiveDashboardImplementation:

    @staticmethod
    def dashboard():

        datasets = (
            HealthcareAnalyticsImplementation
            .load_all_datasets()
        )

        patients_df = datasets["patients"]
        outcomes_df = datasets["outcomes"]
        lab_df = datasets["labs"]
        medications_df = datasets["medications"]

        total_admissions = len(outcomes_df)

        total_medications = int(
            medications_df["patient_id"]
            .nunique()
        )

        total_labs = int(
            lab_df["patient_id"]
            .nunique()
        )

        total_patients = int(
            patients_df["patient_id"]
            .nunique()
        )

        avg_age = round(
            float(
                patients_df["age"].mean()
            ),
            2
        )

        avg_bmi = round(
            float(
                patients_df["bmi"].mean()
            ),
            2
        )

        smoking_rate = round(
            (
                (
                    patients_df[
                        "smoking_status"
                    ] == "Current"
                ).sum()
                /
                len(patients_df)
            ) * 100,
            2
        )

        mortality_rate = round(
            (
                outcomes_df[
                    "in_hospital_death"
                ].fillna(0).sum()
                /
                len(outcomes_df)
            ) * 100,
            2
        )

        htn_patients = (
            patients_df["dx_hypertension"]
            .fillna(0)
            .sum()
        )

        htn_prevalence = round(
            (htn_patients / total_patients) * 100,
            2
        )

        diabetes_patients = int(
        (
                (
                    patients_df["dx_type1_diabetes"]
                    .fillna(0)
                )
                |
                (
                    patients_df["dx_type2_diabetes"]
                    .fillna(0)
                )
            ).sum()
        )

        diabetes_prevalence = round(
            (
                diabetes_patients /
                total_patients
            ) * 100,
            2
        )

        ckd_patients = int(
            patients_df["dx_chronic_kidney_disease"]
            .fillna(0)
            .sum()
        )

        ckd_prevalence = round(
            (
                ckd_patients /
                total_patients
            ) * 100,
            2
        )

        chronic_disease_columns = [

            "dx_hypertension",
            "dx_type2_diabetes",
            "dx_hyperlipidemia",
            "dx_obesity",
            "dx_coronary_artery_disease",
            "dx_heart_failure",
            "dx_atrial_fibrillation",
            "dx_chronic_kidney_disease",
            "dx_copd",
            "dx_asthma",
            "dx_depression",
            "dx_anxiety",
            "dx_hypothyroidism",
            "dx_osteoarthritis",
            "dx_type1_diabetes"
        ]

        patients_df["disease_count"] = (
            patients_df[chronic_disease_columns]
            .fillna(0)
            .sum(axis=1)
        )

        multi_morbid_patients = int(
            (
                patients_df["disease_count"] >= 2
            ).sum()
        )

        total_patients = int(
            patients_df["patient_id"].nunique()
        )

        multi_morbidity_rate = round(
            (
                multi_morbid_patients /
                total_patients
            ) * 100,
            2
        )

        high_bp_patients = (
            (
                patients_df["systolic_bp"] >= 140
            )
            |
            (
                patients_df["diastolic_bp"] >= 90
            )
        ).sum()

        high_bp_rate = round(
            (
                high_bp_patients /
                total_patients
            ) * 100,
            2
        )

        obese_patients = (
            patients_df["bmi"] >= 30
        ).sum()

        obesity_rate = round(
            (
                obese_patients /
                total_patients
            ) * 100,
            2
        )



        abnormal_labs = (
            lab_df["is_abnormal"]
            .fillna(0)
            .sum()
        )

        abnormal_lab_rate = round(
            (
                abnormal_labs /
                total_labs
            ) * 100,
            2
        )

        non_adherent_patients = (
            medications_df[
                "adherence_pct"
            ] < 80
        ).sum()

        non_adherence_rate = round(
            (
                non_adherent_patients /
                total_medications
            ) * 100,
            2
        )

        readmitted_patients = (
            outcomes_df["readmitted_30d"]
            .fillna(0)
            .sum()
        )

        readmission_rate = round(
            (
                readmitted_patients /
                total_admissions
            ) * 100,
            2
        )

        icu_admissions = (
            outcomes_df["icu_admission"]
            .fillna(0)
            .sum()
        )

        icu_admission_rate = round(
            (
                icu_admissions /
                total_admissions
            ) * 100,
            2
        )

        average_los = round(
            float(
                outcomes_df[
                    "length_of_stay_days"
                ].mean()
            ),
            2
        )

        total_cost = (
            outcomes_df["total_charges_usd"]
            .sum()
        )

        avg_cost_per_admission = round(
            total_cost /
            total_admissions,
            2
        )

        threshold = (
            outcomes_df["total_charges_usd"]
            .quantile(0.90)
        )

        high_cost_patients = (
            outcomes_df["total_charges_usd"]
            > threshold
        ).sum()

        high_cost_patient_rate = round(
            (
                high_cost_patients
                /
                len(outcomes_df)
            ) * 100,
            2
        )


        

        readmission_df = outcomes_df[
            outcomes_df["readmitted_30d"] == 1
        ]

        cost_per_readmission = round(
            readmission_df[
                "total_charges_usd"
            ].mean(),
            2
        )

        high_cost_patient_count = int(
            high_cost_patients
        )

        high_cost_total_spend = round(
            outcomes_df.loc[
                outcomes_df["total_charges_usd"] > threshold,
                "total_charges_usd"
            ].sum(),
            2
        )


        executive_metrics = {

            "population_text":
f"""
Patients: {total_patients}
Avg Age: {avg_age}
Avg BMI: {avg_bmi}
Smoking Rate: {smoking_rate}%
""",

            "disease_text":
f"""
HTN Prevalence: {htn_prevalence}
Diabetes Prevalence: {diabetes_prevalence}
CKD Prevalence: {ckd_prevalence}
Multi-Morbidity: {multi_morbidity_rate}
""",

            "clinical_text":
f"""
High BP Rate: {high_bp_rate}
Obesity Rate: {obesity_rate}
Abnormal Labs: {abnormal_lab_rate}
Non-Adherence: {non_adherence_rate}
""",

            "outcomes_text":
f"""
Mortality Rate: {mortality_rate}%
Readmission Rate: {readmission_rate}
ICU Admission Rate: {icu_admission_rate}
Average LOS: {average_los}
""",

            "financial_text":
f"""
Avg Cost/Admission: {avg_cost_per_admission}
Cost/Readmission: {cost_per_readmission}
High Cost Patients: {high_cost_patient_rate}
High Cost Patients Count : {high_cost_patient_count}
High Cost Spend : {high_cost_total_spend}
"""

        }

        return (
            ExecutiveDashboardVisualization
            .generate_dashboard(
                executive_metrics
            )
        )