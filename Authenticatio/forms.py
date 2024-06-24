from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class adduser(UserCreationForm):
    first_name=forms.CharField(max_length=20, required=True)
    last_name=forms.CharField(max_length=20, required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']




class edituser(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']