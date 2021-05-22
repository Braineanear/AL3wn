from django.urls import path
from . import views

urlpatterns  =  [
	path("", views.Home.as_view(), name='ReserveHome'),
	path("view/", views.ApplicantListView.as_view(), name='view'),
	path("report/", views.render_pdf_view, name='report'),
	path("report/<uuid>", views.applicant_render_pdf_view, name='Report'),
	path("<slug:teacher>/<slug:year>/", views.All),
]