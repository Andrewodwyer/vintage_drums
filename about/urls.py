from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name='about'),
    path('edit_about/', views.edit_about, name='edit_about'),
    path('edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]
