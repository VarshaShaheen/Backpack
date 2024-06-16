import datetime
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from app.models import CorporateDocument


def send_email(message, subject):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = " "
    receiver_email = " "
    password = " "

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.preamble = 'This is a multi-part message in MIME format.'

    # Attach the HTML message
    html = render_to_string('email/email.html', {'message': message})
    part_html = MIMEText(html, 'html')
    msg.attach(part_html)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


class Command(BaseCommand):
    help = 'Send email notifications for corporate document expiry'

    def handle(self, *args, **kwargs):
        one_month_from_now = datetime.date.today() + datetime.timedelta(days=30)
        documents_to_notify = CorporateDocument.objects.filter(expiry_date=one_month_from_now)

        for document in documents_to_notify:
            company_detail = document.company
            subject = 'Corporate Document Expiry Reminder'
            message = f"""Dear {company_detail.contact_person_name},

The document '{document.document_name}' ({document.document_number}) associated with your company {company_detail.company_name_en} is expiring on {document.expiry_date}. Please take necessary actions.

Regards,
Backpack"""
            send_email(message, subject)

        self.stdout.write(self.style.SUCCESS('Email notifications sent successfully'))
