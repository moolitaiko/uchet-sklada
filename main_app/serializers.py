from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User


class SkladSerializer(ModelSerializer):
    class Meta:
        model = Sklad
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = ['company_name', 'bin', 'fact_address', 'ur_address', 'telephone']


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ['telephone']