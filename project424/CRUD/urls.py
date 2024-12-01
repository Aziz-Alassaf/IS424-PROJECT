from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),          # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('items/', views.items_view, name='items'),  # Items page
    path('items/<int:pk>/', views.item_detail_view, name='item_detail'),  # Item detail page
    path('items/add/', views.add_item_view, name='add_item'),  # Add item page
]

