from django.urls import path
from .views import send_mail_function

urlpatterns = [
    path('mail', send_mail_function),
]
