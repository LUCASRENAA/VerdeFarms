from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import models
from datetime import  datetime, timezone, timedelta



from core.models import Vendedor,Geolocalizacao,Fazenda,FazendaVendedor,Produto,ProdutoVendedor,FavoritoVendedor,FavoritoProduto,Feira


class LocalizacaoPadrao:
    def __init__(self, ip, quantidade):
        self.ip = ip
        self.quantidade = quantidade


@login_required(login_url='/front/login')

def index(request):
    geos = Geolocalizacao.objects.all()
    feiras = Feira.objects.all()
    for geo in geos:
        try:

            Vendedor.objects.get(usuario=geo.usuario)
        except:
            pass


    dados = {"geos":geos,'feiras':feiras}
    return render(request, "home.html",dados)


def login_user(request):
    return render(request,'login.html')


def registro(request):
    return render(request,'registro.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/front/')
        else:
            messages.error(request,"Usuário ou senha invalido")


    return  redirect('/front')

def submit_registro(request):
    print(request.POST)
    if request.POST:
        senha = request.POST.get('password')
        usuario = request.POST.get ( 'username' )
        email =   request.POST.get ( 'email' )
        try:
            print("e aqui?")


            user = User.objects.create_user ( str(usuario), str(email) ,  str(senha) )




        except:


            return HttpResponse('<h1> Usuario já cadastrado </h1>')

        print("hey")
        return redirect('/front/')
    return HttpResponse('<h1> faça um post </h1>')
