"""VerdeFarms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'is_staff','password']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    queryset = User.objects.all()
    serializer_class = UserSerializer


from core import views
router = routers.DefaultRouter()
router.register('vendedor', views.VendedorViewSet )
router.register('localizacao', views.GeolocalizacaoViewSet )
router.register('fazenda', views.FazendaViewSet )
router.register('fazendaVendedor', views.FazendaVendedorViewSet )
router.register('produto', views.ProdutoViewSet )
router.register('produtoVendedor', views.ProdutoVendedorViewSet )
router.register('favoritoVendedor', views.FavoritoVendedorViewSet)
router.register('favoritoProduto', views.FavoritoProdutoViewSet)
router.register('feira', views.FeiraViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
