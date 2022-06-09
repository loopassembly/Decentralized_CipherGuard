from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request,'test.html')


def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def forgetps(request):
    return render(request,'forget.html')

def password(request):
    return render(request,'password.html')