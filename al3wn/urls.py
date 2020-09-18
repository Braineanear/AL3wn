from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from users.views import register

# Improving DJ Admin
admin.site.site_title = 'AM6 Site Admin'
admin.site.site_header = 'AM6 Administration'
admin.site.index_title = 'AM6 Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fb_bot/', include('fb_bot.urls')),
    path('', include('core.urls')),
    path('register/', register , name="Register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name="Login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name="Logout"),
]
