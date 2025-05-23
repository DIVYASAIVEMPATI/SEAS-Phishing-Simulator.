import smtplib
from email.mime.text import MIMEText

def send_phishing_email(to_email, subject, body):
    sender_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Phishing awareness email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")