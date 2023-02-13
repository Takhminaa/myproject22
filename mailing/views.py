from django.shortcuts import render

# Create your views here.
# myapp/views.py
from .tasks import send_email

def send_newsletter(request):
    subject = "Новости компании"
    html_template = "email_template.html"
    subscribers = [
        "user1@example.com",
        "user2@example.com",
        # ...
    ]

    for email in subscribers:
        send_email.delay(email, subject, html_template, subscribers)