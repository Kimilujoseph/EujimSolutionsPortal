import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import urljoin
from django.utils import timezone
from .models import JobListing

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
}

def scrape_linkedin():
    base_url = "https://www.linkedin.com/jobs/search/"
    searches = [
        {'keywords': 'IT Kenya', 'location': 'Kenya'},
        {'keywords': 'Software Engineer Kenya', 'location': 'Kenya'},
    ]
    
    for search in searches:
        params = {
            'keywords': search['keywords'],
            'location': search['location'],
            'f_TPR': 'r86400',  # Last 24 hours
            'f_JT': 'F',         # Full-time
        }
        
        try:
            response = requests.get(base_url, headers=HEADERS, params=params)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for card in soup.select('.base-card'):
                try:
                    title = card.select_one('.base-search-card__title').get_text(strip=True)
                    company = card.select_one('.base-search-card__subtitle').get_text(strip=True)
                    location = card.select_one('.job-search-card__location').get_text(strip=True)
                    url = card.find('a', class_='base-card__full-link')['href'].split('?')[0]
                    
                    # Save to database
                    JobListing.objects.update_or_create(
                        url=url,
                        defaults={
                            'title': title,
                            'company': company,
                            'location': location,
                            'source': 'LINKEDIN',
                            'job_type': search['location'],
                            'posted_at': timezone.now(),
                            'is_active': True
                        }
                    )
                except Exception as e:
                    continue
                    
        except Exception as e:
            continue

def scrape_careerjet():
    base_url = "https://www.careerjet.co.ke"
    search_url = f"{base_url}/search/jobs?s=IT+OR+Software+OR+Developer&l=Kenya"
    
    try:
        response = requests.get(search_url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for job in soup.select('.job'):
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
                        'is_active': True
                    }
                )
            except Exception as e:
                continue
                
    except Exception as e:
        pass

def scrape_all_jobs():
    scrape_linkedin()
    scrape_careerjet()
    # Mark old jobs as inactive
    JobListing.objects.filter(
        scraped_at__lt=timezone.now()-timedelta(days=14)
    ).update(is_active=False)