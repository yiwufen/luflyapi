# /app/tasks.py
from __future__ import absolute_import, unicode_literals


from celery import shared_task
from captcha.models import CaptchaStore
from django.utils import timezone


@shared_task
def delete_expired_captcha():
    CaptchaStore.objects.filter(expiration__lt=timezone.now()).delete()


