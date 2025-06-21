from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('valider-commande/', views.valider_commande, name='valider_commande'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
