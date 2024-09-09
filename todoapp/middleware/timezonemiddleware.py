import pytz
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Set the default timezone for the request
        timezone.activate(pytz.timezone("Asia/Kolkata"))
        response = self.get_response(request)
        timezone.deactivate()
        return response
