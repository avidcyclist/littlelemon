from rest_framework import serializers
from LittleLemonAPI.models import MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']