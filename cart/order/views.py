from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'order/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, p_slug):
        product = get_object_or_404(Product, slug=p_slug)
        return render(request, 'order/detail.html', {'product': product})
