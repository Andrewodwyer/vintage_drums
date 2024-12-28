from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name='about'),
    path('404/', views.custom_404, name='404_test'),  # Direct URL for testing
    path('edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]