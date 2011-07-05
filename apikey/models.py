from django.db import models
from hashlib import sha1
from random import randint, choice
from string import letters, digits
from django.conf import settings

# Validate TOKEN_SIZE
TOKEN_SIZE = getattr(settings, 'TOKEN_SIZE', 60)


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


class TokenManager(models.Manager):

    def _generate(self):
        return ''.join([choice(letters + digits) for i in range(TOKEN_SIZE)])

    def create(self, user):
        token = self._generate()
        return super(TokenManager, self).create(user=user, token=token)


class Token(models.Model):
    " Token. "

    #: User that creates the token.
    user = models.ForeignKey('auth.User', related_name='api_tokens')

    #: Token.
    token = models.CharField(max_length=TOKEN_SIZE)

    #: IP Address that creates the token.
    ip = models.IPAddressField(null=True, default=None)

    #: Last used time.
    last_used = models.DateTimeField(auto_now=True)

    #: Objects Manager.
    objects = TokenManager()
