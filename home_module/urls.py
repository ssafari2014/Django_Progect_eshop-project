from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_module_View.as_view(), name='index-page'),
]