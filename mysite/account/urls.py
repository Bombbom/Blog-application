from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('login/', views.user_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]