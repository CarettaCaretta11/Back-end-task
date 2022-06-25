from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('account/<str:pk>/', views.my_account, name='my-account')
]