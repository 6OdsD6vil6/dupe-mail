import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email  
    msg['To'] = recipient_email  
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, "your_password")  # Use a more secure method for storing passwords  
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    sender_email = input("Enter sender's email: ")  
    recipient_email = input("Enter recipient's email: ")
    subject = input("Enter subject: ")
    body = input("Enter email body: ")

    send_email(sender_email, recipient_email, subject, body)
