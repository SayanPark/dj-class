from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import UserRegisterForm, UserLoginFrom, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def contact(request):
    return render(request, 'contactus/contact_page.html')


def user_register(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password1'])
            return redirect('home:home-func')
    else:
        form_register = UserRegisterForm()
    context = {'form_register': form_register}
    return render(request, 'contactus/user_register.html', context)


def user_login(request):
    if request.method == 'POST':
        form_login = UserLoginFrom(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home-func')
    else:
        form_login = UserLoginFrom()
    return render(request, 'contactus/login.html', {'form_login': form_login})


def user_logout(request):
    logout(request)
    return redirect('home:home-func')


@login_required()
def change_pass(request):
    if request.method == 'POST':
        user = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            old_pass = data['old_pass']
            new_pass1 = data['new_pass1']
            new_pass2 = data['new_pass2']
            # if old_pass != user.password:
            if not user.check_password(old_pass):
                return HttpResponse('your old password is not correct.')
            elif new_pass1 != new_pass2:
                return HttpResponse('the passwords are not match')
            else:
                user.set_password(new_pass2)
                login(request, user)
                user.save()
                return HttpResponse('password change successfully')
    else:
        form = ChangePasswordForm()

    return render(request,'contactus/Changepass.html', {'form': form})