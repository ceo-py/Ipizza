from rest_framework import serializers

from apps.checkout.models import CartItem, PurchaseHistory, UserProfile


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CartDeleteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['user', 'item_name']
