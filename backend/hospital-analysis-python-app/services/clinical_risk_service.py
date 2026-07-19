from implementations.clinical_risk_impl import (
    ClinicalRiskImplementation
)


class ClinicalRiskService():

    @staticmethod
    def dashboard():

        return (
            ClinicalRiskImplementation
            .dashboard()
        )