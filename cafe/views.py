from rest_framework import generics
from .models import Menu
from .serializers import MenuItemSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class ListMenu(generics.ListCreateAPIView):
    #handles displaying all items in the menu and also allows creating a menu item i.e GET,POST
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name','id']

class DetailMenu(generics.RetrieveUpdateDestroyAPIView):
    #supports update and delete
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer