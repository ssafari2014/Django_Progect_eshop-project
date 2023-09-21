from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contact_Us_View.as_view(), name='contact_us'),
]