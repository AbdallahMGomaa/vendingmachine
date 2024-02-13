from django.db import transaction
from authentication.models import User, Role


class AuthServices:
    @staticmethod
    @transaction.atomic
    def create_user(username, email, password, role):
        user = User.objects.create_user(username=username, email=email, password=password)
        role = Role.objects.create(user=user, name=role)
        return user.id, role.id

