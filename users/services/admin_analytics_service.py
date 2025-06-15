# services/admin_analytics_service.py
from django.db.models import Count, Avg, Q, F, Case, When, IntegerField
from django.db.models.functions import TruncMonth, TruncYear
from datetime import datetime, timedelta
from django.utils import timezone

class AdminAnalyticsService:
    
    def get_dashboard_data(self):
        return {
            "user_metrics": self.get_user_metrics(),
            "skill_metrics": self.get_skill_metrics(),
            "education_metrics": self.get_education_metrics(),
            "certification_metrics": self.get_certification_metrics(),
            "growth_metrics": self.get_growth_metrics(),
            "engagement_metrics": self.get_engagement_metrics(),
            "demographic_metrics": self.get_demographic_metrics()
        }

    def get_user_metrics(self):
        """Key metrics about job seekers using correct field names"""
        from jobseeker.models import JobSeeker
        from users.models import User
        
        total_users = User.objects.filter(role='jobseeker').count()
        
        # Profile completion based on profile updates
        recently_updated_profiles = JobSeeker.objects.filter(
            updatedAt__gte=timezone.now() - timedelta(days=30)
        ).count()
        
        profile_completion = JobSeeker.objects.annotate(
            filled_fields=Count(
                Case(
                    When(~Q(github_url='') & ~Q(github_url=None), then=1),
                    When(~Q(linkedin_url='') & ~Q(linkedin_url=None), then=1),
                    When(~Q(location='') & ~Q(location=None), then=1),
                    When(~Q(bioData='') & ~Q(bioData=None), then=1),
                    output_field=IntegerField()
                )
            )
        ).aggregate(
            avg_completion=Avg(F('filled_fields')/4*100)  # 4 fields total
        )
        
        return {
            "total_job_seekers": total_users,
            "recently_updated_profiles": recently_updated_profiles,
            "avg_profile_completion": profile_completion['avg_completion'] or 0,
            "profiles_added_last_30d": User.objects.filter(
                role='jobseeker',
                createdAt__gte=timezone.now() - timedelta(days=30)  
            ).count()
        }
    def get_engagement_metrics(self):
        """Alternative engagement metrics"""
        from jobseeker.models import JobSeekerCertification, Education
        
        return {
            "certifications_added": JobSeekerCertification.objects.filter(
                createdAt__gte=timezone.now() - timedelta(days=30)
            ).count(),
            "educations_added": Education.objects.filter(
                created_at__gte=timezone.now() - timedelta(days=30)
            ).count(),
            "skills_added": self._get_skills_added_count()
        }
    
    def _get_skills_added_count(self):
        """Count skills added in last 30 days"""
        from skills.models import SkillSet
        return SkillSet.objects.filter(
            createdAt__gte=timezone.now() - timedelta(days=30)
        ).count()

    def get_skill_metrics(self):
        """Skill distribution and proficiency analytics"""
        from skills.models import Skill, SkillSet
        
        top_skills = Skill.objects.annotate(
            user_count=Count('skillset'),
            avg_proficiency=Avg(
                Case(
                    When(skillset__proffeciency_level='begginner', then=1),
                    When(skillset__proffeciency_level='intermediate', then=2),
                    When(skillset__proffeciency_level='midlevel', then=3),
                    When(skillset__proffeciency_level='proffessional', then=4),
                    output_field=IntegerField()
                )
            )
        ).order_by('-user_count')[:10]
        
        return {
            "total_skills": Skill.objects.count(),
            "top_skills": [
                {
                    "skill": skill.skillName,
                    "users": skill.user_count,
                    "avg_proficiency": skill.avg_proficiency or 0
                }
                for skill in top_skills
            ],
            "proficiency_distribution": {
                "beginner": SkillSet.objects.filter(proffeciency_level='begginner').count(),
                "intermediate": SkillSet.objects.filter(proffeciency_level='intermediate').count(),
                "midlevel": SkillSet.objects.filter(proffeciency_level='midlevel').count(),
                "professional": SkillSet.objects.filter(proffeciency_level='proffessional').count()
            }
        }

    def get_education_metrics(self):
        """Education level analytics with safe duration calculation"""
        from jobseeker.models import Education
        from django.db.models import Case, When, Value, F, Avg
        from datetime import datetime
        
        current_year = timezone.now().year
        
        # Safe duration calculation avoiding negative values
        avg_duration = Education.objects.annotate(
            safe_duration=Case(
                # For completed educations
                When(
                    is_current=False,
                    end_year__gte=F('start_year'),
                    then=F('end_year') - F('start_year')
                ),
                # For current educations
                When(
                    is_current=True,
                    start_year__lte=current_year,
                    then=Value(current_year) - F('start_year')
                ),
                # Handle invalid cases
                default=Value(0),
                # output_field=models.IntegerField()
            )
        ).aggregate(
            avg_duration=Avg('safe_duration')
        )['avg_duration'] or 0
        
        # Get degree distribution
        degree_distribution = Education.objects.values('degree').annotate(
            count=Count('id')
        ).order_by('-count')
        
        return {
            "total_educations": Education.objects.count(),
            "degree_distribution": list(degree_distribution),
            "avg_education_years": avg_duration,
            "current_students": Education.objects.filter(is_current=True).count(),
            "invalid_duration_records": Education.objects.filter(
                Q(is_current=False, end_year__lt=F('start_year')) | 
                Q(is_current=True, start_year__gt=current_year)
            ).count()
        }

    def get_certification_metrics(self):
        """Certification analytics"""
        from jobseeker.models import JobSeekerCertification
        
        recent_certs = JobSeekerCertification.objects.filter(
            awarded_date__gte=timezone.now() - timedelta(days=365)
        ).values('issuer').annotate(
            count=Count('id')
        ).order_by('-count')[:5]
        
        return {
            "total_certifications": JobSeekerCertification.objects.count(),
            "top_issuers": list(recent_certs),
            "avg_certs_per_user": JobSeekerCertification.objects.annotate(
                cert_count=Count('user')
            ).aggregate(
                avg=Avg('cert_count')
            )['avg'] or 0
        }

    def get_growth_metrics(self):
        """Platform growth over time"""
        from users.models import User
        from jobseeker.models import JobSeeker
        from skills.models import SkillSet
        
        user_growth = User.objects.filter(
            role='jobseeker',
            createdAt__gte=timezone.now() - timedelta(days=365)
        ).annotate(
            month=TruncMonth('createdAt')
        ).values('month').annotate(
            count=Count('id')
        ).order_by('month')
        
        skill_growth = SkillSet.objects.filter(
            createdAt__gte=timezone.now() - timedelta(days=365)
        ).annotate(
            month=TruncMonth('createdAt')
        ).values('month').annotate(
            count=Count('id')
        ).order_by('month')
        
        return {
            "user_growth": list(user_growth),
            "skill_growth": list(skill_growth)
        }

    def get_demographic_metrics(self):
        """Location and demographic analytics"""
        from jobseeker.models import JobSeeker
        
        locations = JobSeeker.objects.exclude(
            Q(location__isnull=True) | Q(location='')
        ).values('location').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        return {
            "top_locations": list(locations),
            "users_with_location": JobSeeker.objects.exclude(
                Q(location__isnull=True) | Q(location='')
            ).count()
        }