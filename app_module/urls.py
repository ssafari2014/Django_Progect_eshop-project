from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.APP_View.as_view(), name='name_apps_View'),
                  path('profiles/', views.ProfileView.as_view(), name='profiles-view'),
              ]
