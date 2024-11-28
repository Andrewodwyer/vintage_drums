from django.urls import path
from . import views
from .views import ProductListView, product_detail

# urlpatterns = [
#     path('', views.all_products, name='products')
# ]

urlpatterns = [
    path('', ProductListView.as_view(), name='all_products'),
    path('<int:product_id>/', product_detail, name='product_detail'),  # Function-based view
]
