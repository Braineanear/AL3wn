from django.urls import path
from . import views

urlpatterns  =  [
	path("<slug:teacher>/<slug:year>/", views.StudentListView.as_view()),
]