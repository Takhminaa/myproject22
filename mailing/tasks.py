# myapp/tasks.py
from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')


@app.task



def send_email(email, subject, html_template, subscribers):
        pass
    # реализация отправки письма
