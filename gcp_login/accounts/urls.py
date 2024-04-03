from django.urls import path
from . import views

urlpatterns = [
    path('', views.juniper_index, name='juniper_index'),
    path('register/', views.register, name='register'),
    path('register/accounts_list', views.accounts_list, name='accounts_list')
]
