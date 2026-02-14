from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnay, name='glavnay'),
    path('lichni/', views.lichni, name='lichni'),
]