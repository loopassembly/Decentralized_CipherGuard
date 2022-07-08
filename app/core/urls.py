from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.LoginUser, name='login'),
    path('register', views.Signup, name='signup'),
    path('forget', views.forgetps, name='forget'),
    path('password', views.password, name='password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
        
  
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)