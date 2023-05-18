from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_email_thought_celery



@api_view(['GET'])
def send_mail_function(request):
    send_email_thought_celery.delay()
    return Response(status=status.HTTP_200_OK)


