from django.urls import path
from . import views
from .views import creatCheckout

urlpatterns = [
    path('', views.home, name='home-page'),
    path('cart/', views.cart, name='cart-page'),
    path('ordersummary/', views.ordersummary, name='ordersummary-page'),
    path('about/', views.about, name='about-page'),
    path('updateItem/', views.updateItem, name='update-item-page'),
    path('checkOut/', creatCheckout.as_view(), name = 'checkout-page'),
    path('send/', views.send_html_template, name = 'send-page')
]