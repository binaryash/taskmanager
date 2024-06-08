from celery import shared_task
from .CoinMarketCap import CoinMarketCap
from .models import ScrapingJob

# asynchronously scrapes the data and updates the database 
@shared_task
def scrape_coin_data(job_id, coin_acronyms):
    coin_market_cap = CoinMarketCap()
    data = coin_market_cap.scrape(coin_acronyms)
    job = ScrapingJob.objects.get(job_id=job_id)
    job.data = data
    job.completed = True
    job.save()
