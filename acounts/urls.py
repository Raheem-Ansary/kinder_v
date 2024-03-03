from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
   path('register/', views.UserRegisterView.as_view(), name='register_page'),
   path('login/', views.LoginView.as_view(), name='login_page'),
   path('logout/', views.LogoutView.as_view(), name='logout_page'),
   path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
   
]
