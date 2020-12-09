from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import register, profile, career

# Improving DJ Admin
admin.site.site_title = 'AM6 Site Admin'
admin.site.site_header = 'AM6 Administration'
admin.site.index_title = 'AM6 Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fb_bot/', include('fb_bot.urls')),
    path('', include('core.urls')),
    path('careers/', career, name='Career'),
    path('register/', register , name="Register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name="Login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name="Logout"),
    path('profile/', profile, name='Profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html') , name="Password Reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html') , name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html') , name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html') , name="password_reset_complete"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)