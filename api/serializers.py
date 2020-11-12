from core.models import CustomUser, Cart, Product
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'address_shipment', 'cart']


class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    # items = serializers.ReadOnlyField(source='items.pk')

    class Meta:
        model = Cart
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
