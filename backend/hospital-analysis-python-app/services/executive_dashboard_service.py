from implementations.executive_dashboard_impl import (
    ExecutiveDashboardImplementation
)


class ExecutiveDashboardService:

    @staticmethod
    def dashboard():

        return (
            ExecutiveDashboardImplementation
            .dashboard()
        )