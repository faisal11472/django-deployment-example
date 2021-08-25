from django import forms
from django.contrib.auth.models import User
from login.models import UserInfo


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password','email')

class UserprofileInfoForm(forms.ModelForm):

    class Meta():
        model=UserInfo
        fields=('portofolio_site','profile_pic')
