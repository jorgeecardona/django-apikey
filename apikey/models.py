from django.db import models
from hashlib import sha1
from random import randint


class ApiKeyManager(models.Manager):

    def _generate_key(self):
        return sha1(str(randint(0, (16 ** 40) - 1))).hexdigest()

    def generate(self, user):

        # Create
        key = self._generate_key()
        if self.filter(key=key).count() > 0:
            key = self._generate_key()

        return self.create(user=user, key=key)


class ApiKey(models.Model):
    " Api key model."

    #: User that owns the key.
    user = models.ForeignKey('auth.User', related_name='api_keys')

    #: Key.
    key = models.CharField(max_length=40)

    #: Is active?
    is_active = models.BooleanField(default=True)

    # Objects.
    objects = ApiKeyManager()
