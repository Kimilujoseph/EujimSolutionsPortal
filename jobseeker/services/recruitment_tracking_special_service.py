from recruiter.services.recruiter_tracking_base_service import BaseRecruiterTrackingService

class Job_seeker_recruitment_tracking_service(BaseRecruiterTrackingService):
    def __init__(self):
        super().__init__()
        self.role = "job_seeker"
    def  create_tracking(self, user_id: int, data: dict):
        return super().create_tracking(user_id, data, self.role)