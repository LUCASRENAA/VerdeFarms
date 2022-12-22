from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from core.models import Vendedor,Geolocalizacao,Fazenda,FazendaVendedor,Produto,ProdutoVendedor,FavoritoVendedor,FavoritoProduto,Feira

def index(request):
    geo = Geolocalizacao.objects.all()
    dados = {"geo":geo}
    return render(request, "index2.html",dados)