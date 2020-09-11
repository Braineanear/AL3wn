from django.contrib import admin
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
]
