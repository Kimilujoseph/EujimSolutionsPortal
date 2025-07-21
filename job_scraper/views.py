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
        scrape_jobs_task()
        return Response(
            {"status": "Scraping completed"}, 
            status=status.HTTP_202_ACCEPTED
        )
