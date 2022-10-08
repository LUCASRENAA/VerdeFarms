from rest_framework import serializers
from .models import Vendedor,Geolocalizacao,Fazenda,FazendaVendedor,Produto,ProdutoVendedor,FavoritoVendedor,FavoritoProduto,Feira


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'


class GeolocalizacaoSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = FavoritoVendedor
        fields = '__all__'

class FavoritoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritoProduto
        fields = '__all__'

class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = '__all__'