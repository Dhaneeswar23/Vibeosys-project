from rest_framework import serializers
from .models import Products

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__' 
        
    