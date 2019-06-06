from djmoney.money import Money
from rest_framework import  serializers
from .models import Menu

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

