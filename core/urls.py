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
    path('birthdays/', views.Birthdays.as_view(), name='Birthday'),
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
    # Herr Khaled Bakheet
    path('HerrBakheet/', views.herr_bakheet ,name='HerrBakheet'),
    path('HerrBakheet/1/', views.first_bakheet ,name='HerrBakheet1'),
    path('HerrBakheet/2/', views.second_bakheet ,name='HerrBakheet2'),
    path('HerrBakheet/3/', views.third_bakheet ,name='HerrBakheet3'),
    # halem
    path('Halem/3/', views.third_halem, name="Halem3"),
    path('Halem/3/Lesson/', views.halem_lesson, name="HalemLesson"),
    # Bassem
    path('Bassem/1/', views.FirstBassem.as_view(),name='Bassem1'),
    path('Bassem/2/', views.SecondBassem.as_view() ,name='Bassem2'),
    path('Bassem/3/', views.ThirdBassem.as_view() ,name='Bassem3'),
    path('Bassem/up/', views.UpBassem.as_view(),name='BassemUp'),
    path('Bassem/perfect/', views.PerfectBassem.as_view(),name='BassemPerfect'),
    path('Bassem/innovate/', views.InnovateBassem.as_view(),name='BassemInnovate'),
    path("Bassem/videos/", views.VideosBassem.as_view(), name='BassemVideos'),
    path("Bassem/youtube/", views.bassem_youtube, name='BassemYoutube'),
    # Ehab
    path('Ehab/translation/', views.ehab_trans ,name='EhabTranslation'),
    path('EhabElShafey/', views.ehab_elshafey ,name='Ehab'),
    path('Ehab/2/', views.second_ehab ,name='Ehab2'),
    path('Ehab/3/', views.third_ehab ,name='Ehab3')

]