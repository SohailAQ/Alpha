from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)

from product.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product_list.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'manufacturer', 'price', 'quantity', 'purchased_by']


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'manufacturer', 'price', 'quantity', 'purchased_by']


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')
