from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Rest API
# <your_api_app>/urls.py
#from rest_framework.routers import DefaultRouter
#from .views import TaskViewSet
from .views import StatsListCreate 
from .views import StatsDetails 
#from .views import stats_edit   
#from .views import stats_delete


# Change the Django admin site titles
# admin.site.site_header = "My Custom Admin"  # Header text
# admin.site.site_title = "My Site Admin"  # <title> tag on browser tab
# admin.site.index_title = "Welcome to the Admin Portal"  # Main text on the admin index page

DEBUG = False

urlpatterns = [
    path('', views.stats_list, name='stats_list'),
    path('stats_create/', views.stats_create, name='stats_create'), 
    path('<int:customer_id>/edit/', views.stats_edit, name='stats_edit'),
    path('<int:customer_id>/delete/', views.stats_delete, name='stats_delete'),    
    # Include your REST API app's URLs at a specific path, e.g., 'api/'

    #Rest API
    path('stats/', StatsListCreate.as_view(), name='stats-list-create'),
    path('stats/<int:pk>/', StatsDetails.as_view(), name='stats-details'),


    #path('<int:pk>/', views.stats_detail, name='stats_detail'),

    #path('', views.index, name='index'),
    #path('stats/', views.stats_list, name='stats_list'),
    # path('', views.stats_list, name='stats_list'),
    # path('stats/<int:pk>/', views.stats_detail, name='stats_detail'),
    # path('stats/create/', views.stats_create, name='stats_create'), 
    # path('stats/<int:pk>/edit/', views.stats_edit, name='stats_edit'),
    # path('stats/<int:pk>/delete/', views.stats_delete, name='stats_delete'),    

] 
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

