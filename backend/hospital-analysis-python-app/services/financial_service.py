from implementations.financial_impl import (
    FinancialImplementation
)


class FinancialService:

    @staticmethod
    def dashboard():

        return (
            FinancialImplementation
            .dashboard()
        )