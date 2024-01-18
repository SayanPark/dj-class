from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact-us'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('cp/', views.change_pass,name='change-password')
]
