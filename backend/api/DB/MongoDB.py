from django.contrib.auth.backends import BaseBackend
from .models import User  # Import your MongoEngine User model
from django.contrib.auth.hashers import check_password

class MongoDBBackend(BaseBackend):
    """
    Custom authentication backend using MongoEngine.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Look up the user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        # Verify the password
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
