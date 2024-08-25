from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'



urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),
         name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(),name = 'logout'),
    
    path('password_reset_confirm/',views.ChangeFormView.as_view(), name='password_reset_confirm'),
    path('edit/', views.edit, name='edit'),
]
         
