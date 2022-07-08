from django.shortcuts import redirect, render
from .models import Registration, User
from .form import Login, CreateUserForm, CustomerForm
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
from django.core.mail import EmailMessage  # Import the email sending library

# Create your views here.


def test(request):
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
      
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

           # Added username after video because of error returning customer name if not added
            Registration.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(
                request, 'Account was created for ' + username)
             # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('login')
        

    context = {'form': form}
        

    return render(request, 'test.html',context) 


def LoginUser(request):
    context = {}
    form = Login(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            name = request.POST.get('user')
            passw = request.POST.get('passw')
            all = Registration.objects.all().values()
            query = User.objects.filter(username=name).all().values()
            query2 = Registration.objects.all().values()
            userlogin = authenticate(username=name, password=passw)

            print(query, 'query')
            print(query2, 'query')
            print(userlogin)
            if userlogin is not None:
                print('login')
                login(request, userlogin)
                messages.success(request, "Successfully Logged In")
                return redirect("password")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("login")

            # print(test)

    return render(request, "login.html", context)


def Signup(request):
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            
            Registration.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(
                request, 'Account was created for ' + username)
              # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('login')
        

    context = {'form': form}
        

    return render(request, 'signup.html',context) 

    


def forgetps(request):
    return render(request, 'forget.html')


@login_required()
def password(request):
    return render(request, 'password.html')

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  