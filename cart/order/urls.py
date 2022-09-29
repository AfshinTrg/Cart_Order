from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<slug:p_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
