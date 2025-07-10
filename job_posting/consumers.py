from typing import Optional
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from channels_redis.core import RedisChannelLayer
from channels.layers import get_channel_layer
from .models import JobPosting
class JobFeedConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer: Optional[RedisChannelLayer] = None
        self.room_group_name = "job_updates"

    async def connect(self):
        # Initialize channel layer with proper typing
        self.channel_layer = get_channel_layer()
        
        if not self.channel_layer:
            await self.close(code=4001)
            return

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send initial data
        jobs = await self.get_job_listings()
        await self.send_json({
            'type': 'initial_jobs',
            'jobs': jobs
        })

    async def disconnect(self, close_code):
        # Leave room group with null check
        if self.channel_layer:
            try:
                await self.channel_layer.group_discard(
                    self.room_group_name,
                    self.channel_name
                )
            except Exception as e:
                print(f"Group discard error: {e}")

    @database_sync_to_async
    def get_job_listings(self):
       
        return list(JobPosting.objects.filter(is_active=True).values(
            'id', 'title', 'company', 'location'
        ))