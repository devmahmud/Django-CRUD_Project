from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:book_id>', views.edit, name='edit'),
    path('delete/<int:book_id>', views.delete, name='delete'),
]
