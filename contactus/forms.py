from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Enter a unique username'}))
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Confirm your password'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user existed before')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل تکراری است')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('passwords are not match')
        elif len(password2)<8:
            raise forms.ValidationError('پسوورد کمتر از هشت حرف است')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('پسوورد باید دارای حداقل یک حرف بزرگ باشد')
        else:
            return password1


class UserLoginFrom(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass1 = forms.CharField(widget=forms.PasswordInput())
    new_pass2 = forms.CharField(widget=forms.PasswordInput())

