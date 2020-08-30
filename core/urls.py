from django.urls import path
from . import views

urlpatterns  =  [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('dev/', views.dev, name='Dev'),
    path('pricing/', views.price, name='Price'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('sec/', views.sec, name='Secondary'),
    path('stage1/', views.stage1, name="Stage1"),
    path('stage2/', views.stage2, name="Stage2"),
]