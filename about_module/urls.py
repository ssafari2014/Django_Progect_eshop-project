from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_View.as_view(), name='about-page'),
]