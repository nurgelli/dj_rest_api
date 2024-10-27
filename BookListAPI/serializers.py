from rest_framework import serializers
from . models import BookItem
from decimal import Decimal


class BookItemSerializers(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    class Meta:
        model = BookItem
        # fields = '__all__'
        fields = ['id', 'price', 'stock', 'price_after_tax']
    def calculate_tax(self, product:BookItem):
        return product.price
        