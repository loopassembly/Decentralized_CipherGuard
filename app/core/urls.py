from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.test, name='test'),
    path('', views.login, name='login'),
    path('register', views.signup, name='signup'),
    path('forget', views.forgetps, name='forget'),
    path('password', views.password, name='password'),
  
]