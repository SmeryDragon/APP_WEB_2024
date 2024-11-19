from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.wishlist_view, name='wishlist_view'),
    path('add/', views.add_product, name='add_product'),
]
