from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_View.as_view(), name='register-page'),
    path('login', views.Login_View.as_view(), name='login-page'),
    path('logout', views.Logout_View.as_view(), name='logout-page'),
    path('active_account/<str:email_active_code>', views.Active_Account_View.as_view(), name='active_account-page'),
    path('reset_account/<str:email_active_code>', views.Reset_Password_View.as_view(), name='reset-page'),
    path('forgot_password', views.Forgot_Password_View.as_view(), name='forgot-page'),

]
