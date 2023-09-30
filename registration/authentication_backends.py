from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from api import models
from .models import Healthworker

class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to get a healthworker using either email or phone number
            healthworker = Healthworker.objects.get(
                models.Q(email=username) | models.Q(phone_number=username)
            )
        except Healthworker.DoesNotExist:
            # If no healthworker is found, return None
            return None

        # Check the password against the healthworker's password
        if healthworker.check_password(password):
            return healthworker

    def get_user(self, user_id):
        try:
            return Healthworker.objects.get(pk=user_id)
        except Healthworker.DoesNotExist:
            return None
