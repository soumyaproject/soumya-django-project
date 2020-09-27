from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import signupform
# Create your views here.
@login_required
def java_view(request):
    return render(request,'testapp/javaexam.html')
def home_view(request):
    return render(request,'testapp/home.html')
def logout_view(request):
    return render(request,'testapp/logout.html')
def sign_view(request):
    form=signupform()
    return render(request,'testapp/signup.html',{'form':form})
