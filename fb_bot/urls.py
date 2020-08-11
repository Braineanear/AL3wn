from django.urls import path
from django.conf.urls import include, url
from .views import FBBotView

urlpatterns = [
    url('72864ad91191769dd244272b5e235e6378e6baceaa77329883/?$', FBBotView.as_view())
]
