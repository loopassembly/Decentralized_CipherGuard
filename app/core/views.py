from django.shortcuts import render

# Create your views here.

def tempview(request):
    return render(request,'index.html')