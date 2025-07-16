from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import JobListing
from .serializers import JobListingSerializer
from .tasks import scrape_jobs_task

class JobListAPIView(generics.ListAPIView):
    queryset = JobListing.objects.filter(is_active=True)
    serializer_class = JobListingSerializer
    filterset_fields = ['source', 'location', 'company']

class TriggerScrapeAPIView(generics.GenericAPIView):
    def post(self, request):
        # Trigger async scraping
        scrape_jobs_task.delay()
        return Response(
            {"status": "Scraping initiated"}, 
            status=status.HTTP_202_ACCEPTED
        )
