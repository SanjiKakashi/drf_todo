from datetime import datetime

import pytz
from django.utils import timezone


def now():
    return timezone.now().astimezone(pytz.timezone("Asia/Kolkata"))


def make_aware(datetime_obj):
    if timezone.is_naive(datetime_obj):
        return timezone.make_aware(datetime_obj, timezone=pytz.timezone("Asia/Kolkata"))
    return datetime_obj
