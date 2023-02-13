from django.db import models

# Create your models here.
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


from celery import task

@app.task
def send_email(email, message):
    # Code to send email goes here
    pass

from datetime import timedelta

send_email.apply_async(args=
                       ['recipient@example.com', 'Hello, World!'],
                       countdown=timedelta(minutes=30))