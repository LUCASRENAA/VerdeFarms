from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Vendedor(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)

    apelido = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)


class Geolocalizacao(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    usuario = models.ForeignKey(User, models.CASCADE)


class Fazenda(models.Model):
    fazenda = models.CharField(max_length=50)
    agrotoxico = models.BooleanField()
    descricao = models.CharField(max_length=50)


class FazendaVendedor(models.Model):
    vendedor = models.ForeignKey(Vendedor, models.CASCADE)
    fazenda = models.ForeignKey(Fazenda, models.CASCADE)


class Produto(models.Model):
    nome = models.CharField(max_length=50)


class ProdutoVendedor(models.Model):
    produto = models.ForeignKey(Produto, models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    descricao = models.CharField(max_length=50)
    ter_ou_nao = models.BooleanField()


class FavoritoVendedor(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)

    vendedor = models.ForeignKey(Vendedor, models.CASCADE)


class FavoritoProduto(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)
    produto = models.ForeignKey(Produto, models.CASCADE)


class Feira(models.Model):
    nome = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    data_evento = models.DateTimeField(auto_now=True)


"""
class Feira(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=8)
    complemento = models.CharField(max_length=8)
    bairro = models.CharField(max_length=8)
    localidade = models.CharField(max_length=8)
    uf = models.CharField(max_length=8)
    
"""
