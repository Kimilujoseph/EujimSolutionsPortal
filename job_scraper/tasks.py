from celery import shared_task
from .utils import scrape_all_jobs

@shared_task
def scrape_jobs_task():
    """Celery task for scraping jobs"""
    scrape_all_jobs()
    return "Job scraping completed"