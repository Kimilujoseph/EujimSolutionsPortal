from  ..repository.educationRepository import EducationRepository
from django.core.exceptions import ValidationError

class EducationService:
    def __init__(self):
        self.education_repo = EducationRepository()

    def create_education(self, user_id: int, education_data: dict):
        education_data['user_id'] = user_id
        print(f"Creating education for user {user_id} with data: {education_data}")
        return self.education_repo.create(**education_data)

    def update_education(self, education_id: int, user_id: int, update_data: dict):
        return self.education_repo.update_education(education_id, user_id, update_data)

    def delete_education(self, education_id: int, user_id: int):
        education = self.education_repo.filter(id=education_id, user_id=user_id).first()
        if education:
            self.education_repo.delete(education)
            return True
        return False

    def get_user_educations(self, user_id: int):
        return self.education_repo.get_educations_by_user(user_id)
    def get_education_distribution(self, user_id: int):
        try:
            return self.education_repo.get_education_distribution(user_id)
        except ValidationError as e:
            print(f"Validation error: {e}")
            return []
        except Exception as e:
            print(f"An error occurred while fetching education distribution: {e}")
            return []