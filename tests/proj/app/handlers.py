from apikey.auth import TokenAuthentication
from piston.handler import BaseHandler
from piston.resource import Resource
from app.models import Item


class ItemHandler(BaseHandler):
    allowed_methods = ('GET', )
    fields = ('name', 'id')
    model = Item

    def read(self, request):
        return Item.objects.all()

handler = Resource(
    handler=ItemHandler, authentication=TokenAuthentication())
