# services/recruiter_analytics_service.py
from django.db.models import Count, Case, When, IntegerField, F, Q, ExpressionWrapper, DurationField, Avg, Max, Subquery, OuterRef
from django.db.models.functions import TruncDay, Coalesce
from datetime import timedelta
from django.utils import timezone
from django.db import connection
from ..repository.recruiter_repository import RecruiterRepository, RecruiterTrackingRepository, RecruiterDocRepository

class RecruiterAnalyticsService:
    def __init__(self, recruiter_id):
        self.recruiter_id = recruiter_id
        self.tracking_repo = RecruiterTrackingRepository()
        self.doc_repo = RecruiterDocRepository()
        self.recruiter_repo = RecruiterRepository()

    def get_dashboard_data(self):
        recruiter = self.recruiter_repo.get_by_id(self.recruiter_id)
        if not recruiter:
            return None
        
        return {
            "recruitment_overview": self.get_recruitment_overview(),
            "candidate_pipeline": self.get_candidate_pipeline(),
            "performance_metrics": self.get_performance_metrics(),
            "document_status": self.get_document_status(),
            "recent_activities": self.get_recent_activities(),
            "skill_insights": self.get_skill_insights()
        }

    def get_recruitment_overview(self):
        """Key recruitment metrics"""
        tracking = self.tracking_repo.get_by_recruiter(self.recruiter_id)
        total_candidates = tracking.values('job_seeker_id').distinct().count()
        
        status_counts = tracking.values('status').annotate(
            count=Count('id', distinct=True)
        )
        
        status_map = {item['status']: item['count'] for item in status_counts}
        
        return {
            'total_candidates': total_candidates,
            'hired': status_map.get('hired', 0),
            'interviewed': status_map.get('interviewed', 0),
            'shortlisted': status_map.get('shortlisted', 0),
            'rejected': status_map.get('rejected', 0),
        }

    def get_candidate_pipeline(self):
        """Breakdown of candidates by stage using MySQL-compatible approach"""
        # Raw SQL for maximum MySQL compatibility
        raw_query = """
            SELECT status, COUNT(*) as count
            FROM (
                SELECT t1.job_seeker_id, t1.status
                FROM recruiter_tracking t1
                INNER JOIN (
                    SELECT job_seeker_id, MAX(updatedAt) as max_updated
                    FROM recruiter_tracking
                    WHERE recruiter_id = %s
                    GROUP BY job_seeker_id
                ) t2 ON t1.job_seeker_id = t2.job_seeker_id AND t1.updatedAt = t2.max_updated
                WHERE t1.recruiter_id = %s
            ) latest_status
            GROUP BY status
        """
        
        with connection.cursor() as cursor:
            cursor.execute(raw_query, [self.recruiter_id, self.recruiter_id])
            rows = cursor.fetchall()
        
        return {status: count for status, count in rows}

    def get_performance_metrics(self):
        """Time-based performance metrics"""
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        
        # Weekly activity
        weekly_activity = self.tracking_repo.get_by_recruiter(self.recruiter_id).filter(
            updatedAt__gte=thirty_days_ago
        ).annotate(
            day=TruncDay('updatedAt')
        ).values('day').annotate(
            actions=Count('id')
        ).order_by('day')
        
        # Conversion rates (simplified without previous_status)
        total_shortlisted = self.tracking_repo.get_by_recruiter(self.recruiter_id).filter(
            status='shortlisted'
        ).count()
        
        # Count all interviewed candidates (regardless of previous status)
        interviewed_count = self.tracking_repo.get_by_recruiter(self.recruiter_id).filter(
            status='interviewed'
        ).count()
        
        return {
            'weekly_activity': list(weekly_activity),
            'interviewed_count': interviewed_count,
            'shortlisted_count': total_shortlisted,
            'avg_time_to_respond': self.calculate_avg_response_time()
        }

    def calculate_avg_response_time(self):
        """Calculate average time between candidate actions using subquery approach"""
        # Get previous update time for each tracking record
        prev_update_subquery = self.tracking_repo.get_by_recruiter(self.recruiter_id).filter(
            job_seeker_id=OuterRef('job_seeker_id'),
            updatedAt__lt=OuterRef('updatedAt')
        ).order_by('-updatedAt').values('updatedAt')[:1]
        
        # Annotate with previous update time
        tracking_with_prev = self.tracking_repo.get_by_recruiter(self.recruiter_id).annotate(
            prev_update=Subquery(prev_update_subquery)
        ).exclude(prev_update__isnull=True)
        
        # Calculate response times
        response_times = tracking_with_prev.annotate(
            response_time=ExpressionWrapper(
                F('updatedAt') - F('prev_update'),
                output_field=DurationField()
            )
        ).aggregate(
            avg_response=Avg('response_time')
        )
        
        return response_times['avg_response'] or timedelta(0)

    def get_document_status(self):
        """Document verification status"""
        docs = self.doc_repo.get_by_recruiter(self.recruiter_id)
        status_counts = docs.values('status').annotate(count=Count('id'))
        
        return {
            'total_documents': docs.count(),
            'pending': next((item['count'] for item in status_counts if item['status'] == 'pending'), 0),
            'approved': next((item['count'] for item in status_counts if item['status'] == 'approved'), 0),
            #'latest_document': docs.order_by('-updatedAt').first()
        }

    def get_recent_activities(self, limit=5):
        """Recent candidate interactions"""
        return list(self.tracking_repo.get_by_recruiter(self.recruiter_id)
            .order_by('-updatedAt')
            .values(
                'job_seeker__user__firstName',
                'job_seeker__user__lastName',
                'status',
                'updatedAt',
                'notes'
            )[:limit]
        )

    def get_skill_insights(self):
        """Top skills from tracked candidates using optimized raw SQL"""
        raw_query = """
            SELECT 
                s.skillName AS skill,
                COUNT(ss.id) AS count,
                AVG(
                    CASE ss.proffeciency_level
                        WHEN 'begginner' THEN 1
                        WHEN 'intermediate' THEN 2
                        WHEN 'midlevel' THEN 3
                        WHEN 'proffessional' THEN 4
                        ELSE 0
                    END
                ) AS avg_proficiency
            FROM recruiter_tracking rt
            JOIN job_seeker js ON rt.job_seeker_id = js.id
            JOIN users u ON js.users_id = u.id
            JOIN skillSet ss ON u.id = ss.userId
            JOIN skills s ON ss.skill_id = s.id
            WHERE rt.recruiter_id = %s
            GROUP BY s.skillName
            ORDER BY count DESC
            LIMIT 5
        """
        
        with connection.cursor() as cursor:
            cursor.execute(raw_query, [self.recruiter_id])
            rows = cursor.fetchall()
        
        return [
            {
                'skill': row[0],
                'count': row[1],
                'avg_proficiency': float(row[2]) if row[2] is not None else 0
            }
            for row in rows
        ]