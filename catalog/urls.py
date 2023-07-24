from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contact'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
]


