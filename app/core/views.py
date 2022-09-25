from ast import Pass
from datetime import timezone
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views import View
from requests import request
from .models import Registration, User , Userpassword
from .form import Login, CreateUserForm, CustomerForm ,CreatePasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .tokens import account_activation_token  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.template.loader import render_to_string 
from django.http import HttpResponse   
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.contrib.auth import get_user_model 
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.utils.html import strip_tags
from django.core import mail
from .localvar import LocalV
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
import datetime
from tzlocal import get_localzone_name
from django.utils.timezone import get_current_timezone, make_aware, now
from cryptography.fernet import Fernet
from django.http import JsonResponse
from django.contrib.auth import logout
import string    
from . import temp_functions
import random # define the random module 
# Create your views here.
def email(email):
    return




def LoginUser(request):
   
    print(LocalV.lcount,'starting')
    form = Login(request.POST or None)
    context = {
        'form':form,
        'email_status': True}

    # if request.user.is_authenticated:
    #     return password(request)
    if request.POST:
        if form.is_valid():
            name = request.POST.get('username')
            request.session['username'] = name
            passw = request.POST.get('passw')
            all = Registration.objects.all().values()
            query = User.objects.filter(username=name).all().values()
            query2 = Registration.objects.all().values()
            userlogin = authenticate(username=name, password=passw)

            if userlogin is not None:
                login(request, userlogin)
                messages.success(request, "Successfully Logged In")
                return redirect("password")
            else:
                if User.objects.filter(username=name).values():
                    usr=User.objects.get(username=name)
                    if usr.is_active==False :
                        messages.error(request, "Email not verified")
                        context = {
                                'form':form,
                                'email_status': False
                                }
                        return render(request, 'login.html', context)
                
                    
                else:
                    messages.error(request, "Invalid Username or Password!")
                    return redirect("login")
        
        if request.POST.get('email_val') == 'email':
           
            if LocalV.lcount<2:
                print(LocalV.lcount,'test')
                print('running')
                LocalV.lcount_inc()
                
                email_sent(request)
                return render(request, 'email_confirm.html',{'user_email':User.objects.get(username=request.session['username']).email})
                    
            else:
                print(LocalV.lcount)
                LocalV.lcount=0
                print('after',LocalV.lcount)
                return render(request, 'login.html',context)
            # print(test)
    else:
        return render(request, "login.html", context)
    return render(request, "login.html", context)


def forgetps(request):
    return render(request, 'forget.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required()
def password(request):
    
    current_user = request.user
    form = CreatePasswordForm(request.POST or None)
    context = {
        'form':form,
    }
    if request.user.is_authenticated:
        pasword=Userpassword.objects.filter(user=current_user).values()
        
     
        context ={
            'user':current_user,
            'password':pasword,
            'localtime':get_localzone_name(),
            'form':form,
            
        }
       
        if request.POST:
            if form.is_valid():
                platform = request.POST.get('platform')
                password = request.POST.get('password')
                key = Fernet.generate_key()
                
                fernet = Fernet(key)
                
                encpassword = fernet.encrypt(password.encode())
                # decodedstr=encpassword.decode()
                
                Userpassword.objects.create(platform=platform, password=encpassword, decrpt_key=key, user=current_user)
                messages.success(request, "Password Created Successfully")
                return redirect("password")                                                             
            elif request.POST.get('update')=='update':
                enckpassword=request.POST.get('editpass')
                # password incryption
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encpassword_new = fernet.encrypt(enckpassword.encode())

                updaterec=Userpassword.objects.get(id=request.POST.get('id'))
                updaterec.platform=request.POST.get('editplt')
                updaterec.password=encpassword_new 
                updaterec.decrpt_key=key
                updaterec.save()
                messages.success(request, "Successfully updated")
                return redirect("password")

        return render(request, 'password.html', context)
    return render(request, 'password.html',context)

def Signup(request):
        
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('username')
        request.session['username'] = name
        user_email= request.POST.get('email')
        request.session['email'] = user_email

        context = {'data': request.POST,'form': form}
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            
             # set to false to make active after email confirmation
            username = form.cleaned_data.get('username')
             
            Registration.objects.create(
                    user=user,
                    name=user.username,
                )
            user.is_active = False
            user.save()
            messages.success(
                    request, 'Account was created for ' + username)
                
                
            email_sent(request)
            
            return render(request, 'email_confirm.html',{'user_email':request.session['email']})
        else:
            return render(request, 'signup.html',context)  
            

    context = {'form': form}
            

    return render(request, 'signup.html',context) 

    



def email_sent(request): 
    
    if request.session.has_key('username'):   
      
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('acc_active_email.html', {  
                                'user': User.objects.get(username=request.session['username']),  
                                'domain': current_site.domain,  
                                'uid':urlsafe_base64_encode(force_bytes(User.objects.get(username=request.session['username']).pk)),  
                                'token':account_activation_token.make_token(User.objects.get(username=request.session['username'])),  
                            })  
        plain_message = strip_tags(message)
        to_email = User.objects.get(username=request.session['username']).email
        
        mail.send_mail(subject=mail_subject, message=plain_message,  recipient_list=[to_email] ,html_message=message,  from_email=None) 
        context = {
                'data': 'sent email',
                'email':to_email
            }
        return render(request, 'email_confirm.html',context)
    else:
        return HttpResponse('Something went wrong!')
    # return render(request, 'email_confirm.html')
   


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid =  force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request,'emailcon.html')
    else:  
        return render(request, 'email_fail.html')

def viewer(request):
    return render(request, 'emailcon.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        current_site = get_current_site(request)  
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':current_site.domain,
                        
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                       send_mail(subject, email, from_email=None,  recipient_list=[user.email], fail_silently=False)
                        
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
            else:
                context = {
                    "password_reset_form":password_reset_form,
                    'form_error': "No user associated with this email",
                    'user_email':data

                }
                return render(request, 'password/password_reset.html', context)
    
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

def receivedata(request):
  
   
    if request.method == "GET":
        
        encMessage = bytes(request.GET.get("password", None), 'utf-8')
        decryptkey=bytes(request.GET.get("decrypt_key", None),'utf-8')
        fernet = Fernet(decryptkey)
        decMessage = fernet.decrypt(encMessage
        ).decode()
     
        return JsonResponse({"decrypted_password":decMessage}, status = 200)
        
        
    return JsonResponse({}, status = 400)

def deleteRecord(request):
    if request.method == "POST":
        id=request.POST.get('record-del')
        print(id)
        Userpassword.objects.get(id=id).delete()  

    return  HttpResponse('hell')
    
def UpdateRec(request):
    if request.method=='POST':
        id=request.POST.get('record-del')
        pass
def stpassword(request):
    if request.method == "GET":
        
        encMessage = request.GET.get("data")
        if encMessage=='generate':
            return JsonResponse({"spassword":temp_functions.strpassword()}, status = 200)
        
        
    return JsonResponse({}, status = 400)
    
def password_change(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
         
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                
                    return redirect ("/password_reset/done/")
            else:
                
                return render(request, 'password/password_reset.html', )
    
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

    # return render(request,'password/password_reset_witout_email.html')
@login_required()
def pass_reset_sucess(request,num):
    
    

    return render(request,'password/password_reset_complete.html' ,{'num':num})
