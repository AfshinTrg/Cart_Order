from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
]
