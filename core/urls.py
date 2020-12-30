from django.urls import path
# from django.conf.urls import handler404

from . import views

# handler404 = 'core.views.not_found'


urlpatterns  =  [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('dev/', views.dev, name='Dev'),
    path('pricing/', views.price, name='Price'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('sec/', views.sec, name='Secondary'),
    path('youtube/', views.youtube),
    path('stage1/', views.stage1, name="Stage1"),
    path('stage2/', views.stage2, name="Stage2"),
    # Deutsch Akademie
    path('HerrShady/1/', views.first_shady, name="HerrShady1"),
    path('HerrShady/2/', views.second_shady, name="HerrShady2"),
    path('HerrShady/3/', views.third_shady, name="HerrShady3"),
    # halem
    path('Halem/3/', views.third_halem, name="Halem3")

]