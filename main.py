from scraper.amazon_scraper import AmazonScraper
from database.db_handler import DatabaseHandler
from analysis.price_analyzer import PriceAnalyzer
from notification.email_notifier import EmailNotifier
from datetime import datetime

def main():
    amazon_scraper = AmazonScraper()
    db_handler = DatabaseHandler()
    price_analyzer = PriceAnalyzer(db_handler)
    email_notifier = EmailNotifier('your_email@gmail.com', 'your_password')

    product_url = 'https://www.amazon.com/dp/B08F7PTF53'
    product_data = amazon_scraper.scrape_product(product_url)
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    db_handler.insert_product(product_data['title'], product_data['price'], current_date)

    if price_analyzer.check_price_drop(product_data['title']):
        history = db_handler.get_product_history(product_data['title'])
        current_price = history[0][0]
        previous_price = history[1][0]
        
        email_notifier.send_price_drop_alert(
            'recipient@example.com',
            product_data['title'],
            current_price,
            previous_price
        )

    price_analyzer.generate_price_trend(product_data['title'])

    db_handler.close()

if __name__ == '__main__':
    main()
