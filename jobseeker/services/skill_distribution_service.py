from ..repository.recruiter_interaction import RecruiterInteraction
from ..repository.skill_repository import SkillDistributionSet, SkillSetRepository
from users.exceptions import NotFoundException, ServiceException, InternalErrorException
from typing import Dict, List, Any, Optional
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

class SkillAnalyticsService:
    def __init__(self):
        self.recruiter_repo = RecruiterInteraction()
        self.skill_distribution_repo = SkillDistributionSet()
        self.skill_set_repo = SkillSetRepository()

    def skill_distribution(self, job_seeker_id: int) -> Dict[str, int]:
      

        self._validate_job_seeker_id(job_seeker_id)
        
        try:
            distribution = self.skill_distribution_repo.get_skill_distribution(job_seeker_id)
            if not distribution:
                raise NotFoundException("No skill distribution found for this user")
            
            result = {
                'beginner': 0,
                'intermediate': 0,
                'midlevel': 0,
                'professional': 0
            }
            
            for item in distribution:
                try:
                    level = item['proffeciency_level']
                    result[level] = item['count']
                except (KeyError, TypeError) as e:
                    logger.warning(f"Invalid skill distribution format: {e}")
                    continue
            
            return result
            
        except DatabaseError as e:
            logger.error(f"Database error in skill_distribution: {str(e)}", 
                       extra={'job_seeker_id': job_seeker_id})
            raise InternalErrorException("Failed to fetch skill distribution") from e
        except Exception as e:
            logger.error(f"Unexpected error in skill_distribution: {str(e)}")
            raise InternalErrorException("Skill distribution calculation failed") from e

    def get_skills_growth_timeline(self, job_seeker_id: int) -> List[Dict[str, str]]:
  
        self._validate_job_seeker_id(job_seeker_id)
        
        try:
            skills = self.skill_distribution_repo.get_skill_set(job_seeker_id)
            if not skills:
                return []
                
            timeline = []
            for skill in skills:
                try:
                    entry = {
                        'skill_name': self._get_skill_name_from_model(skill),
                        'proficiency_level': skill.proffeciency_level,
                        'date_added': self._format_model_date(skill.createdAt)
                    }
                    timeline.append(entry)
                except AttributeError as e:
                    logger.warning(f"Invalid skill object format: {e}", 
                                extra={"skill_id": getattr(skill, 'id', None)})
                    continue
                    
            return sorted(timeline, key=lambda x: x['date_added'])
            
        except DatabaseError as e:
            logger.error(f"Database error fetching skill timeline: {str(e)}")
            raise InternalErrorException("Failed to fetch skill timeline") 
        except Exception as e:
            logger.error(f"Unexpected error processing skill timeline: {str(e)}")
            raise InternalErrorException("Skill timeline processing failed")


    # Helper methods
    def _validate_job_seeker_id(self, job_seeker_id: int) -> None:
        """Validate job seeker ID format"""
        if not isinstance(job_seeker_id, int) or job_seeker_id <= 0:
            raise ServiceException("Invalid job seeker ID format")
    def _get_skill_name_from_model(self, skill) -> str:
        if skill.skill and hasattr(skill.skill, 'skillName'):
            return skill.skill.skillName
        return 'Unknown'

    def _format_model_date(self, date_obj) -> str:
        """Format date from model field"""
        if date_obj and hasattr(date_obj, 'strftime'):
            return date_obj.strftime('%Y-%m-%d')
        return ''

    def _format_date(self, date_obj: Any) -> str:
        if hasattr(date_obj, 'strftime'):
            return date_obj.strftime('%Y-%m-%d')
        return str(date_obj)[:10] if date_obj else ''