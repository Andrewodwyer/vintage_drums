from django.urls import path
from . import views
from .views import product_detail

# urlpatterns = [
#     path('', views.all_products, name='products')
# ]

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', product_detail, name='product_detail'),  # Function-based view int as it is a number
]
