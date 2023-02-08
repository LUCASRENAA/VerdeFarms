from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny

# Create your views here.
from core.models import Vendedor,Geolocalizacao,Fazenda,FazendaVendedor,Produto,ProdutoVendedor,FavoritoVendedor,FavoritoProduto,Feira


from core.serializers import VendedorSerializer, GeolocalizacaoSerializer, FazendaSerializer, FazendaVendedorSerializer, \
    ProdutoSerializer, ProdutoVendedorSerializer, FavoritoVendedorSerializer, FavoritoProdutoSerializer, \
    FeiraSerializer, RegisterSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )
    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(usuario=request.user)

    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']


class GeolocalizacaoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(usuario=request.user)


    queryset = Geolocalizacao.objects.all()
    serializer_class = GeolocalizacaoSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']


class FazendaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']



class FazendaVendedorViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = FazendaVendedor.objects.all()
    serializer_class = FazendaVendedorSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']



class ProdutoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']



class ProdutoVendedorViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = ProdutoVendedor.objects.all()

    def perform_create(self, serializer):
        request = serializer.context["request"]
        print(request)
        print( Vendedor.objects.get(usuario=request.user))
        serializer.save(vendedor = Vendedor.objects.get(usuario=request.user))

    serializer_class = ProdutoVendedorSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']



class FavoritoVendedorViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = FavoritoVendedor.objects.all()
    serializer_class = FavoritoVendedorSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']



class FavoritoProdutoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = FavoritoProduto.objects.all()
    serializer_class = FavoritoProdutoSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']


class FeiraViewSet(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.IsAuthenticated, )

    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']





class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer