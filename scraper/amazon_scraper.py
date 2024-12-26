import requests
from bs4 import BeautifulSoup

class AmazonScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_product(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('span', {'id': 'productTitle'}).text.strip()
        price = soup.find('span', {'class': 'a-price-whole'}).text.strip()

        return {
            'title': title,
            'price': float(price.replace(',', ''))
        }
