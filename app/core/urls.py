from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import reverse_lazy,reverse
from . import temp_functions

temp=temp_functions.ranstr()
urlpatterns = [
    # path('test', views.test, name='test'),
    path('', views.LoginUser, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.Signup, name='signup'),
    path('forget', views.forgetps, name='forget'),
    path('password', views.password, name='password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('register/resend',views.email_sent,name='email_sent'),
    path('viewer', views.viewer),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('decrypt',views.receivedata, name='decrypt'),
    path('password_change', views.password_change,name='password_change'),
    path(f"password-reset-sucess/<slug:num>",views.pass_reset_sucess,name='pss-sucess'),
    path('delete-record/',views.deleteRecord,name='delete-rec'),
    path('update-record/',views.UpdateRec,name='updaterec'),
    path('strpassword',views.stpassword,name='stpass'),

     # password reset urls
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      
    path(
        'complete-password',
        auth_views.PasswordChangeView.as_view(
            template_name='password/password_reset_witout_email.html',
            success_url = f'password-reset-sucess/{temp}'
            # success_url = reverse('pss-sucess')
            
        ),
        name='change_password'
    )
    
        
  
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)