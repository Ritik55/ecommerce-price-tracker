## E-commerce Price Tracker

A robust web scraping tool that monitors product prices on major e-commerce platforms, analyzes price trends, and sends alerts for price drops.

### Features

- Web scraping from Amazon (expandable to eBay and Walmart)
- Daily price tracking and storage
- Price trend visualization
- Email notifications for significant price drops
- SQLite database for data persistence

### Technologies Used

- Python
- BeautifulSoup
- Requests
- SQLite
- Matplotlib
- smtplib (for email notifications)

### Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ecommerce-price-tracker.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure email settings in `main.py`

4. Run the script:
   ```
   python main.py
   ```

### Future Enhancements

- Add support for eBay and Walmart
- Implement a user interface for easy product tracking
- Integrate with a cloud database for scalability

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is open source and available under the [MIT License](LICENSE).
