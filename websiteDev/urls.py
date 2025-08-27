"""
URL configuration for websiteDev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# custom admin sites
#from fetchStats.admin import my_admin_site


# Change the Django admin site titles
admin.site.site_header = "Nahdi Online"  # Header text
admin.site.site_title = "My Site Admin"  # <title> tag on browser tab
admin.site.index_title = "Welcome to the admin Portal"  # Main text on the admin index page


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', my_admin_site.urls),
    path('fetchStats/', include('fetchStats.urls')),
    #path('fetchStats/', include('fetchStats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
