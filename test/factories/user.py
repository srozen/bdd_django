import factory
from django.contrib.auth.models import User
# This is directly bound to the User model from Django !


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    # Defaults (can be override)
    username = 'john.doe'
    email = 'john.doe@example.com'
