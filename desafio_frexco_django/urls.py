"""desafio_frexco_django URL Configuration

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
from django.urls import path
from cadastrar_cliente import views
from django.views.generic import RedirectView

from django.urls import include, path

from rest_framework import routers
from cadastrar_cliente.api import CustomerViewSet

api_router = routers.DefaultRouter()
api_router.register(r"customers", CustomerViewSet)
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/all/', views.liste_all_customer),
    path('customer/detail/<id>/', views.customer_detail),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('customer/register/', views.register_customer),
    path('customer/register/submit', views.set_customer),
    path('customer/delete/<id>/', views.delete_customer),
    path('', RedirectView.as_view(url='customer/all/')),
    path('api/', include(api_router.urls)),
]
