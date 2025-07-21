import requests
import time
import random
import logging
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import urljoin
from django.utils import timezone
from .models import JobListing

# Set up logging
logger = logging.getLogger(__name__)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
}

# Constants
MAX_PAGES = 10  # Safety limit to prevent infinite loops
REQUEST_DELAY = (2, 5)  # Random delay range between requests (seconds)
RECENT_DAYS = 7  # Only scrape jobs posted in last 7 days

def make_request(url, params=None):
    """Helper function to make HTTP requests with error handling"""
    try:
        delay = random.uniform(*REQUEST_DELAY)
        time.sleep(delay)
        response = requests.get(url, headers=HEADERS, params=params, timeout=15)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {url}: {str(e)}")
        return None

def scrape_linkedin():
    """Scrape job listings from LinkedIn with proper pagination"""
    base_url = "https://www.linkedin.com/jobs/search/"
    searches = [
        {'keywords': 'IT Kenya', 'location': 'Kenya'},
        {'keywords': 'Software Engineer Kenya', 'location': 'Kenya'},
        {'keywords': 'Developer Kenya', 'location': 'Kenya'},
        {'keywords': 'Data Analyst Kenya', 'location': 'Kenya'},
        {'keywords': 'IT Remote', 'location': 'Remote'},
        {'keywords': 'Software Engineer Remote', 'location': 'Remote'},
        {'keywords': 'Developer Remote', 'location': 'Remote'},
        {'keywords': 'Data Analyst Remote', 'location': 'Remote'},
    ]
    
    for search in searches:
        page = 0
        has_more_pages = True
        jobs_count = 0
        
        logger.info(f"Scraping LinkedIn for: {search['keywords']} in {search['location']}")
        
        while has_more_pages and page < MAX_PAGES:
            params = {
                'keywords': search['keywords'],
                'location': search['location'],
                'f_TPR': f'r{86400 * RECENT_DAYS}',  # Filter by recent days
                'f_JT': 'F',  # Full-time only
                'start': page * 25,  # LinkedIn shows 25 jobs per page
            }
            
            response = make_request(base_url, params)
            if not response:
                has_more_pages = False
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            job_cards = soup.select('.base-card')
            
            if not job_cards:
                has_more_pages = False
                logger.info("No more jobs found, moving to next search")
                break
                
            for card in job_cards:
                try:
                    title = card.select_one('.base-search-card__title').get_text(strip=True)
                    company = card.select_one('.base-search-card__subtitle').get_text(strip=True)
                    location = card.select_one('.job-search-card__location').get_text(strip=True)
                    url = card.find('a', class_='base-card__full-link')['href'].split('?')[0]
                    
                    JobListing.objects.update_or_create(
                        url=url,
                        defaults={
                            'title': title,
                            'company': company,
                            'location': location,
                            'source': 'LINKEDIN',
                            'job_type': search['location'],
                            'posted_at': timezone.now(),
                            'scraped_at': timezone.now(),
                            'is_active': True
                        }
                    )
                    jobs_count += 1
                except Exception as e:
                    logger.warning(f"Failed to process LinkedIn job card: {str(e)}")
                    continue
            
            # Check for next page availability
            next_button = soup.select_one('button[aria-label="Next"]')
            if not next_button or 'disabled' in next_button.get('class', []):
                has_more_pages = False
            else:
                page += 1
                
        logger.info(f"Finished scraping LinkedIn. Found {jobs_count} jobs for {search['keywords']}")

def scrape_careerjet():
    """Scrape job listings from CareerJet with proper pagination"""
    base_url = "https://www.careerjet.co.ke"
    search_queries = [
        {'s': 'IT OR Software OR Developer', 'l': 'Kenya'},
        {'s': 'Data Analyst OR Data Scientist', 'l': 'Kenya'},
        {'s': 'IT OR Developer', 'l': 'Remote'},
    ]
    
    for query in search_queries:
        page = 1
        has_more_pages = True
        jobs_count = 0
        search_url = f"{base_url}/search/jobs"
        
        logger.info(f"Scraping CareerJet for: {query['s']} in {query['l']}")
        
        while has_more_pages and page <= MAX_PAGES:
            params = {**query, 'p': page}
            response = make_request(search_url, params)
            
            if not response:
                has_more_pages = False
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            jobs = soup.select('.job')
            
            if not jobs:
                has_more_pages = False
                logger.info("No more jobs found, moving to next search")
                break
                
            for job in jobs:
                try:
                    title = job.select_one('h2').get_text(strip=True)
                    company = job.select_one('.company').get_text(strip=True)
                    location = job.select_one('.location').get_text(strip=True)
                    url = job.find('a')['href']
                    
                    if not url.startswith('http'):
                        url = urljoin(base_url, url)
                    
                    JobListing.objects.update_or_create(
                        url=url,
                        defaults={
                            'title': title,
                            'company': company,
                            'location': location,
                            'source': 'CAREERJET',
                            'posted_at': timezone.now(),
                            'scraped_at': timezone.now(),
                            'is_active': True
                        }
                    )
                    jobs_count += 1
                except Exception as e:
                    logger.warning(f"Failed to process CareerJet job: {str(e)}")
                    continue
            
            # Check for next page
            next_link = soup.select_one('a.next')
            if not next_link:
                has_more_pages = False
            else:
                page += 1
                
        logger.info(f"Finished scraping CareerJet. Found {jobs_count} jobs for {query['s']}")

def scrape_all_jobs():
    """Main function to run all scrapers"""
    logger.info("Starting job scraping process")
    
    try:
        scrape_linkedin()
        scrape_careerjet()
        
        # Mark old jobs as inactive
        cutoff_date = timezone.now() - timedelta(days=RECENT_DAYS)
        old_jobs = JobListing.objects.filter(
            scraped_at__lt=cutoff_date,
            is_active=True
        )
        
        count = old_jobs.update(is_active=False)
        logger.info(f"Marked {count} old jobs as inactive")
        
    except Exception as e:
        logger.error(f"Error in scrape_all_jobs: {str(e)}")
        raise
    
    logger.info("Job scraping process completed")