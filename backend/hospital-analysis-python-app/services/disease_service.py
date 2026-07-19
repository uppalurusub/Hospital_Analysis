from implementations.disease_impl import (
    DiseaseImplementation
)


class DiseaseService:

    # =====================================================
    # Top Diseases
    # =====================================================

    def get_top_diseases():

        return DiseaseImplementation.top_diseases()

    # =====================================================
    # Hypertension
    # =====================================================

    def get_hypertension_prevalence():

        return DiseaseImplementation.hypertension_prevalence()

    # =====================================================
    # Type 2 Diabetes
    # =====================================================

    def get_type2_diabetes_prevalence():

        return DiseaseImplementation.type2_diabetes_prevalence()

    # =====================================================
    # CKD
    # =====================================================

    def get_ckd_prevalence():

        return DiseaseImplementation.ckd_prevalence()

    # =====================================================
    # CAD
    # =====================================================

    def get_cad_prevalence():

        return DiseaseImplementation.cad_prevalence()

    # =====================================================
    # Heart Failure
    # =====================================================

    def get_heart_failure_prevalence():

        return DiseaseImplementation.heart_failure_prevalence()

    # =====================================================
    # COPD
    # =====================================================

    def get_copd_prevalence():

        return DiseaseImplementation.copd_prevalence()

    # =====================================================
    # Asthma
    # =====================================================

    def get_asthma_prevalence():

        return DiseaseImplementation.asthma_prevalence()

    # =====================================================
    # Depression
    # =====================================================

    def get_depression_prevalence():

        return DiseaseImplementation.depression_prevalence()

    # =====================================================
    # Anxiety
    # =====================================================

    def get_anxiety_prevalence():

        return DiseaseImplementation.anxiety_prevalence()

    # =====================================================
    # Obesity
    # =====================================================

    def get_obesity_prevalence():

        return DiseaseImplementation.obesity_prevalence()

    # =====================================================
    # Comorbidity Analysis
    # =====================================================

    def get_comorbidity_analysis():

        return DiseaseImplementation.comorbidity_analysis()

    # =====================================================
    # Chronic Disease Burden
    # =====================================================

    def get_chronic_disease_burden():

        return DiseaseImplementation.chronic_disease_burden()
    
    @staticmethod
    def dashboard():

        return (
            DiseaseImplementation
            .generate_dashboard()
        )
    
    