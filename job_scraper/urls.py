from django.urls import path
from .views import JobListAPIView, TriggerScrapeAPIView

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='job-list'),
    path('scrape/', TriggerScrapeAPIView.as_view(), name='trigger-scrape'),
]