from django.http import HttpResponse
from django.contrib.auth import get_user_model

from quiz.tasks import mine_bitcoin, normalize_email_task


def bitcoin(request):
    mine_bitcoin.delay()
    return HttpResponse("Task is started")


def normalize_email(request):
    normalize_email_task.delay(filter={"email__endswith": ".com"})
    return HttpResponse("Task is started")
