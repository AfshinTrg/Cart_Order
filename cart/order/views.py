from django.shortcuts import render
from django.views import View
from .models import Product, Category


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'order/home.html', {'products': products, 'categories': categories})

