"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('countries', CountriesListView.as_view(), name='countries_list_url'),
    # path('customers', CustomersListView.as_view(), name='customers_list_url'),
    # path('products', ProductsListView.as_view(), name='products_list_url'),
    # path('country_detail/<int:pk>', CountriesDetailView.as_view(), name='countries_detail_url'),
    # path('product_detail/<int:pk>', ProductDetailView.as_view(), name='products_detail_url'),
    # path('countries_create', CountriesCreateView.as_view(), name='countries_create_url'),
    # path('products_create', ProductsCreateView.as_view(), name='products_create_url'),
    # path('countries_delete/<int:pk>', CountriesDeleteView.as_view(), name='countries_delete_url'),
    # path('countries_update/<int:pk>', CountriesUpdateView.as_view(), name='countries_update_url'),
    # path('', MainTemplateView.as_view(), name='main_url'),
    path('sklad_search', SearchApiView.as_view()),
    path('otdo', OtAdoYaApiView.as_view()),
    path('across',AcrossSkladProductApiView.as_view()),
    path('regist', RegistrationApiView.as_view()),
    path('auth', AuthApiView.as_view()),
    path('sellerregist', SellerRegistrationApiView.as_view()),
    path('printcheck', PrintCheck.as_view()),
    path('product', CreateProductApiView.as_view()),
    path('me', UserApiView.as_view()),
    path('me/owner-profile', OwnerApiView.as_view()),
    path('me/seller-profile', SellerApiView.as_view()),
]
