

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import UserSignUpForm
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def signup_view(request):
    if request.method =='POST':
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()

            login(request,user)
            return redirect('purpose:home')
    else:
        form=UserSignUpForm()
    return render(request,'accounts/signup.html',{'form':form,})


def login_view(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('purpose:home')
    else:
        form= AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:login')
