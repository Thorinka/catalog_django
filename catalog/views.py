from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': "Все товары",
    }

class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.product_name

        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}) : {message}")

    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)

# def product(request, pk):
#     product_list = Product.objects.filter(id=pk)
#     context = {
#         'object_list': product_list,
#         'title': Product.objects.get(id=pk)
#     }
#     return render(request, 'catalog/product_detail.html', context)
