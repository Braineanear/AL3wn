from django.urls import path
from . import views

urlpatterns  =  [
	path("<slug:slug>/", views.TeacherView.as_view(), name="Teacher"),
	path("<slug:teacher>/<slug:year>/", views.StudentListView.as_view(), name='Year'),
	path("<slug:teacher>/<slug:year>/<slug:classe>/<slug:student>/", views.StudentPage, name='Student'),

]