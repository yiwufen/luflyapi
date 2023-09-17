# /celery_app.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery



# from lufly.apps.user.tasks import delete_expired_captcha


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lufly.settings.dev')

# from lufly.apps.user.tasks import delete_expired_captcha

app = Celery('lufly_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
# print(settings)
# app.register_task(delete_expired_captcha)
app.autodiscover_tasks()


