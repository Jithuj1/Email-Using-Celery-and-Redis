from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind =True)
def send_email_thought_celery(self):
    print('here it is celery')
    send_mail(
        'hello',
        'Hello habibi come to kochi',
        'jtietshiun@gmail.com',
        ['jithujacob73@gmail.com', 'salmonjacob51@gmail.com'],
        fail_silently=False,
    )

