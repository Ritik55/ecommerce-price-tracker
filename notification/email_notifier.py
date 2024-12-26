import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotifier:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_price_drop_alert(self, recipient_email, product_title, current_price, previous_price):
        subject = f"Price Drop Alert: {product_title}"
        body = f"""
        The price of {product_title} has dropped!
        
        Previous price: ${previous_price:.2f}
        Current price: ${current_price:.2f}
        
        Check it out now!
        """

        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)
