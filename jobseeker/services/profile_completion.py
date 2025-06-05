from ..repository.jobseeker_repository import   JobSeekerRepository
from ..repository.educationRepository import EducationRepository
JobSeekerRepository = JobSeekerRepository()
EducationRepository = EducationRepository()

def calculate_profile_completion(job_seeker_id: int) :

    jobseeker = JobSeekerRepository.get_by_user_id(job_seeker_id)
    if not jobseeker:
        return 0
    
    fields_to_check ={
        jobseeker.github_url,
        jobseeker.linkedin_url,
        jobseeker.location,
        jobseeker.bioData,
        jobseeker.about

    }
  
    has_education   = EducationRepository.get_educations_by_user(job_seeker_id)
    if has_education:
        fields_to_check.add('education')
    else:
        fields_to_check.add('no_education')

   
    filled_fields = sum(1 for field in fields_to_check if field)
    total_fields = len(fields_to_check)
    if total_fields == 0:
        return 0  
    completion_percentage = (filled_fields / total_fields) * 100
    return int(completion_percentage)  