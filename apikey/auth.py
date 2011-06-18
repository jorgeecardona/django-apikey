from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from apikey.models import ApiKey


class ApiKeyAuthentication(object):

    def is_authenticated(self, request):
        " Check if request is authenticated."

        auth_header = getattr(
            settings, 'APIKEY_AUTHORIZATION_HEADER', 'Authorization')

        auth_header = ('Http-%s' % (auth_header, )).upper().replace('-', '_')

        if auth_header not in request.META:
            return False

        auth_string = request.META.get(auth_header)

        try:
            key = ApiKey.objects.get(key=auth_string, is_active=True)
            request.user = key.user
            return True
        except ApiKey.DoesNotExist:
            request.user = AnonymousUser()
            return False

    def challenge(self):
        resp = HttpResponse('Authorization Required')
        resp.status_code = 401
        return resp
