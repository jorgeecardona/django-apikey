django-apikey
=============
Key authentication for django. Can be used with django-piston easily.

Based on https://github.com/scoursen/django-apikey.


Installation
------------
::

    pip install django-apikey


Configuration
-------------

Add 'apikey' to your settings.py:
::

    INSTALLED_APPS = (
    ...
    'apikey',
    ....
    )


You can change the authorization header by setting the APIKEY_AUTHORIZATION_HEADER in settings.py:
::

    APIKEY_AUTHORIZATION_HEADER = 'App-Authorization'


To add api authentication with piston do thisin your handlers.
::

    from apikey.auth import ApiKeyAuthentication
    from piston.handler import BaseHandler
    from piston.resource import Resource
    from myapp.models import Item
    
    class ItemHandler(BaseHandler):
        allowed = ('GET', )
        model = Item
    
        def read(self):
            return Item.objects.all()
    
    handler = Resource(
        handler=ItemHandler, authentication=ApiKeyAuthentication())


Thanks
------

This project is base on the one of Steve Course https://github.com/scoursen/django-apikey but with several simplifications.

License
-------

This software is licensed  under the New BSD License.
