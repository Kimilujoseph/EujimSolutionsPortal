from ..repository.recruiter_interaction import  RecruiterInteraction;
from ..repository.skill_repository import SkillDistributionSet,SkillSetRepository

#initalize the repositories 
RecruiterInteraction = RecruiterInteraction()
SkillDistribution = SkillDistributionSet()
SkillSetRepository = SkillSetRepository()

def skill_distribution(job_seeker_id:int):
    try:
        distribution = SkillDistribution.get_skill_distribution(job_seeker_id)
        result = {
            'begginner': 0,
            'intermediate': 0,
            'midlevel': 0,
            'proffessional': 0
        }
        
        for item in distribution:
            result[item['proffeciency_level']] = item['count']
        
        return result
    except Exception as e:
        print(f"Error fetching skill distribution: {e}")
        return {
            'begginner': 0,
            'intermediate': 0,
            'midlevel': 0,
            'proffessional': 0
        }



#top skill by application rate

def get_top_skills_by_success(job_seeker_id: int):
    try:
        applications = RecruiterInteraction.get_application_status(job_seeker_id)
        user_skills = SkillDistribution.get_skill_set(job_seeker_id)
        
        if not user_skills or not applications:
            return []

        # First map applications to their outcomes
        app_outcomes = {}
        for app in applications:
            if hasattr(app, 'id'):  # Model instance
                app_id = app.id
                status = app.status
            else:  # Dictionary-like
                app_id = app.get('id')
                status = app.get('status')
            app_outcomes[app_id] = status in ['interviewed', 'hired']
        
        # Then count skill associations with successful apps
        skill_stats = {}
        for skill in user_skills:
            if hasattr(skill, 'skill'):  # Model instance
                skill_id = skill.skill.id if skill.skill else None
                skill_name = skill.skill.skillName if skill.skill else 'Unknown'
                proficiency = skill.proffeciency_level
                app_id = skill.application_id  # You'll need this relationship
            else:  # Dictionary-like
                skill_id = skill.get('skill_id')
                skill_name = skill.get('skill__name', 'Unknown')
                proficiency = skill.get('proffeciency_level')
                app_id = skill.get('application_id')
            
            if not skill_id or not app_id:
                continue
                
            if skill_id not in skill_stats:
                skill_stats[skill_id] = {
                    'name': skill_name,
                    'proficiency': proficiency,
                    'associated_apps': set(),
                    'positive_outcomes': 0
                }
            
            # Track unique applications per skill
            skill_stats[skill_id]['associated_apps'].add(app_id)
            
            # Count if this application was successful
            if app_outcomes.get(app_id, False):
                skill_stats[skill_id]['positive_outcomes'] += 1
        
        # Calculate success rates
        results = []
        for skill_id, data in skill_stats.items():
            total_apps = len(data['associated_apps'])
            positive = data['positive_outcomes']
            success_rate = (positive / total_apps) * 100 if total_apps > 0 else 0
            
            results.append({
                'skill_id': skill_id,
                'skill_name': data['name'],
                'proficiency': data['proficiency'],
                'success_rate': round(success_rate, 2),
                'total_applications': total_apps
            })
        
        return sorted(results, key=lambda x: x['success_rate'], reverse=True)[:10]
    
    except Exception as e:
        print(f"Error in get_top_skills_by_success: {e}")
        return []
def get_skills_growth_timeline(job_seeker_id: int):
    
    try:
        skills = SkillDistribution.get_skill_set(job_seeker_id)
        print(f"Skills for user {job_seeker_id}: {skills}")
        if not skills:
            return []
        
        growth_timeline = []
        
        for skill in skills:
           
            if hasattr(skill, 'skill'):  
                skill_name = skill.skill.skillName if skill.skill else 'Unknown'
                proficiency = skill.proffeciency_level
                created_at = skill.createdAt
            else: 
                skill_name = skill.get('skill__name', 'Unknown')
                proficiency = skill.get('proffeciency_level')
                created_at = skill.get('createdAt')
            
           
            date_str = ''
            if created_at:
                if hasattr(created_at, 'strftime'):  
                    date_str = created_at.strftime('%Y-%m-%d')
                else: 
                    date_str = str(created_at)[:10] 
            
            growth_timeline.append({
                'skill_name': skill_name,
                'proficiency_level': proficiency,
                'date_added': date_str
            })
        
        return sorted(growth_timeline, key=lambda x: x['date_added'])
    except Exception as e:
        print(f"Error fetching skills growth timeline: {e}")
        return []

