from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from .cart import Cart
from .forms import CartAddForm


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'order/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, p_slug):
        product = get_object_or_404(Product, slug=p_slug)
        form = CartAddForm()
        return render(request, 'order/detail.html', {'product': product, 'form': form})


class CartView(View):

    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, p_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=p_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart')


