from implementations.outcomes_impl import (
    OutcomesImplementation
)


class OutcomesService:

    @staticmethod
    def dashboard():

        return (
            OutcomesImplementation
            .dashboard()
        )