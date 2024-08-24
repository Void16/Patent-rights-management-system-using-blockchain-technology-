from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patent_register, name='patent_register'),
    path('all/', views.patent_list, name='patent_list'),
    path('my-patents/', views.user_patents, name='user_patents'),
]
