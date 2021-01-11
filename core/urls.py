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
    path('HerrShady/', views.herr_shady, name="HerrShady"),
    path('HerrShady/Lesson/', views.shady_lesson, name='HerrShadyLesson'),
    path('HerrShady/1/', views.first_shady, name="HerrShady1"),
    path('HerrShady/2/', views.second_shady, name="HerrShady2"),
    path('HerrShady/3/', views.third_shady, name="HerrShady3"),
    # AliRashed
    path('HerrAliRashed/', views.herr_ali ,name='HerrAli'),
    path('HerrAliRashed/1/', views.first_ali ,name='HerrAli1'),
    path('HerrAliRashed/2/', views.second_ali ,name='HerrAli2'),
    path('HerrAliRashed/3/', views.third_ali ,name='HerrAli3'),
    # Mohamed Abdel Atty
    path('HerrM/', views.herr_m ,name='HerrM'),
    path('HerrM/1/', views.first_m ,name='HerrM1'),
    path('HerrM/2/', views.second_m ,name='HerrM2'),
    path('HerrM/3/', views.third_m ,name='HerrM3'),
    # halem
    path('Halem/3/', views.third_halem, name="Halem3"),
    path('Halem/3/Lesson/', views.halem_lesson, name="HalemLesson"),
    # Bassem
    path('Bassem/1/', views.first_bassem ,name='Bassem1'),
    path('Bassem/2/', views.second_bassem ,name='Bassem2'),
    path('Bassem/3/', views.third_bassem ,name='Bassem3'),
    path('Bassem/up/', views.bassem_up ,name='BassemUp'),
    path('Bassem/perfect/', views.bassem_perfect ,name='BassemPerfect'),
    path("Bassem/youtube/", views.bassem_youtube, name='BassemYoutube'),
    # Ehab
    path('EhabElShafey/', views.ehab_elshafey ,name='Ehab'),
    path('Ehab/2/', views.second_ehab ,name='Ehab2'),
    path('Ehab/3/', views.third_ehab ,name='Ehab3')

]