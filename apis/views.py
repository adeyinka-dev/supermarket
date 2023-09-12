from rest_framework import generics
from items.models import Item
from .serializers import ItemSerializer


class ItemAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
