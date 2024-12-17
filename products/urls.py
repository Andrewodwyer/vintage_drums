from django.urls import path
from . import views
from .views import product_detail

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/like/', views.toggle_like, name='toggle_like'), #like toggle
    path('<int:product_id>/', product_detail, name='product_detail'),  # Function-based view int as it is a number
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
