from implementations.healthcare_impl import (
    HealthcareAnalyticsImplementation
)

class HealthcareAnalyticsService:

    @staticmethod
    def load_datasets():

        return HealthcareAnalyticsImplementation.validate_all()