import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

load_dotenv()

class EmailSender:
    def __init__(self, sender_email, password, smtp_server='smtp.gmail.com', port=587):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, receiver_email, subject, body, image_path, signature_image_path):
        msg = MIMEMultipart("related")
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the HTML body
        msg.attach(MIMEText(body, "html"))

        # Attach the first image
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<image1>')  # Referencing the first image
            img.add_header('Content-Disposition', 'inline', filename="image.png")
            msg.attach(img)

        # Attach the signature image
        with open(signature_image_path, 'rb') as sign_file:
            sign_img = MIMEImage(sign_file.read())
            sign_img.add_header('Content-ID', '<signImage>')  # Referencing the signature image
            sign_img.add_header('Content-Disposition', 'inline', filename="sign.png")
            msg.attach(sign_img)

        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()

if __name__ == "__main__":
    sender_email = os.getenv("Email_username")
    password = os.getenv("Email_password")
    receiver_email = os.getenv("Email_Recipient")
    subject = "Urgent: Fax Automation Issue"
    body = open('Template/email_template.html', 'r').read()  # Read your HTML template
    image_path = 'Template/image.png'  # Path to the first image
    signature_image_path = 'Template/sign.png'  # Path to the signature image

    email_sender = EmailSender(sender_email, password)
    email_sender.send_email(receiver_email, subject, body, image_path, signature_image_path)