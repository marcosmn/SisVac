"""sisvac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework import routers
from django.contrib.auth.models import User
from vacinacao import views
from vacinacao import loginviews

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'agendamentos', views.AgendamentoViewSet)
router.register(r'fila', views.FilaDeEsperaViewSet)
router.register(r'carteira', views.CarteiraViewSet, basename=views.CarteiraSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    #path('', include('vacinacao.urls')),
    #path('', TemplateView.as_view(template_name='index.html')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/v1/', include(router.urls)),
    path('api/v1/currentuser/', loginviews.UserLoginViewSet.as_view(), name='currentuser'),
    path('api/v1/currentuser/logout', loginviews.UserLogout.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path('api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]
