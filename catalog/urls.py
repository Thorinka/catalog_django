from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contact'),
    path('products/<int:pk>/', product, name='product'),
]


