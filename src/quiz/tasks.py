import random
import time

from celery import shared_task
from django.contrib.auth import get_user_model


@shared_task
def mine_bitcoin():
    time.sleep(random.randint(1, 10))


@shared_task
def normalize_email_task(filter):
    query_set = get_user_model().objects.filter(**filter)
    if query_set:
        for user in query_set:
            print(f"working with user: {user.email}")
            user.save()
    else:
        print("empty data")
