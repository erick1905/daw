from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *

def landing(request):
    template_to_return='landing.html'
    context={
        'view_name': "landing"
    }
    return render(request, template_to_return,context)

def home (request):
    template_to_retun= "home.html"
    return render (request , template_to_retun)


def login_usuario(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)
def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        form = CreateUserForm()
        if request.method=='POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'La cuenta ha sido creada para:'+ user)
                return redirect('login')

        context={'form':form}
        return render(request,'register.html',context)