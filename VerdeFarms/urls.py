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
#Serializer to Get User Details using Django Token Authentication
from core.views import RegisterUserAPIView


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username",'email']
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #talvez realmente não precise botar autenticação para ver isso, pois, um usuário tem que ver os dados dos outros usuários
    #permission_classes = (permissions.IsAuthenticated, )


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


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/register', RegisterUserAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("front/", include("front.urls")),

]
