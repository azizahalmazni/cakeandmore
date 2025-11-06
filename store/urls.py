from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('custom/', views.custom_cake, name='custom_cake'),
]
