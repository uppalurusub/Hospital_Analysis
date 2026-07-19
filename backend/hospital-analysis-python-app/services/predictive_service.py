from implementations.predictive_impl import (
    PredictiveImplementation
)


class PredictiveService:

    @staticmethod
    def dashboard():

        return (
            PredictiveImplementation
            .dashboard()
        )