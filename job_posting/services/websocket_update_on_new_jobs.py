from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from typing import Optional
from django.core.exceptions import ObjectDoesNotExist
from channels_redis.core import RedisChannelLayer

def notify_new_job(job):
    
    try:
        
        channel_layer: Optional[RedisChannelLayer] = get_channel_layer()
        
        if channel_layer is None:
            raise RuntimeError("Channel layer not configured properly")
        
       
        if not all(hasattr(job, attr) for attr in ['id', 'title', 'company', 'location', 'posted_at']):
            raise ValueError("Invalid job object provided")

      
        company_name = job.company.name if hasattr(job.company, 'name') else "Unknown Company"
        
        async_to_sync(channel_layer.group_send)(
            'job_updates',
            {
                'type': 'job.update',  # Must match consumer method name
                'job': {
                    'id': str(job.id),
                    'title': str(job.title),
                    'company': company_name,
                    'location': str(job.location),
                    'posted_at': job.posted_at.isoformat(),
                    'action': 'added'
                }
            }
        )
    except ObjectDoesNotExist as e:
        print(f"Job related object missing: {e}")
    except AttributeError as e:
        print(f"Missing required job attribute: {e}")
    except Exception as e:
        print(f"Failed to notify about new job: {e}")