# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import (
   authenticate,
   get_user_model,
   login,
   logout,
)
from .forms import UserLoginForm,UserRegistrationForm,User

# Create your views here.
def login_view(request):
    title="Login"
    if not request.user.is_authenticated() :
        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            #login is directly used for logging in.
            login(request,user)
            return redirect("/")
        query_set= User.objects.all()
        context = {"form":form,"title":title,"list":query_set}
        return render(request,"forms.html",context)
    return redirect("/")

def register_view(request):
    title = "Register"
    form  = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        return redirect("/")

    query_set = User.objects.all()
    context = {"form":form,"title":title,"list":query_set}

    return render(request,"forms.html",context)


def logout_view(request):
    logout(request)
    return redirect("/")
