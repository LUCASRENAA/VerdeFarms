from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Vendedor,Geolocalizacao,Fazenda,FazendaVendedor,Produto,ProdutoVendedor,FavoritoVendedor,FavoritoProduto,Feira


class VendedorSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Vendedor
        fields = '__all__'


class GeolocalizacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    class Meta:
        model = Geolocalizacao
        fields = '__all__'


class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = '__all__'


class FazendaVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FazendaVendedor
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoVendedor
        fields = '__all__'


class FavoritoVendedorSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = FavoritoVendedor
        fields = '__all__'

class FavoritoProdutoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = FavoritoProduto
        fields = '__all__'

class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = '__all__'


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user