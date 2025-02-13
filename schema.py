import strawberry

@strawberry.type
class DeploymentFrequency:
    week: str
    count: int

@strawberry.type
class LeadTimeForChanges:
    average_days: float

@strawberry.type
class ChangeFailureRate:
    percentage: float

@strawberry.type
class Metrics:
    deployment_frequency: DeploymentFrequency
    lead_time_for_changes: LeadTimeForChanges
    change_failure_rate: ChangeFailureRate

    @strawberry.field
    def deployment_frequency(self) -> DeploymentFrequency:
        return DeploymentFrequency(week="2025-W08", count=15)

    @strawberry.field
    def lead_time_for_changes(self) -> LeadTimeForChanges:
        return LeadTimeForChanges(average_days=3.2)

    @strawberry.field
    def change_failure_rate(self) -> ChangeFailureRate:
        return ChangeFailureRate(percentage=5.4)

@strawberry.type
class Query(Metrics):
    pass

schema = strawberry.Schema(query=Query)