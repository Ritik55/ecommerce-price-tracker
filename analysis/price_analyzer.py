import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class PriceAnalyzer:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def generate_price_trend(self, title):
        history = self.db_handler.get_product_history(title)
        dates = [datetime.strptime(date, '%Y-%m-%d') for _, date in history]
        prices = [price for price, _ in history]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, prices)
        plt.title(f'Price Trend for {title}')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{title}_price_trend.png')
        plt.close()

    def check_price_drop(self, title, threshold=0.1):
        history = self.db_handler.get_product_history(title)
        if len(history) < 2:
            return False

        current_price = history[0][0]
        previous_price = history[1][0]
        
        price_drop = (previous_price - current_price) / previous_price
        return price_drop >= threshold
