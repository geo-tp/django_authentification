from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import HttpResponse
from authentification.models import CustomUser as User
import datetime
import pytz
from django.utils import timezone
from rest_framework import status

def hidePartOfData(data):

    return data[0:1] + '****' + data[-1:]


def hidePartOfPaymentMethod(payment_data):

    if payment_data:

        return "*"*12+payment_data[-4:]

    else:
        return payment_data


def custom_create_token(token_model, user, serializer):
    token = token_model.objects.create(user=user)
    utc_now = timezone.now()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    token.created = utc_now
    token.save()
    return token