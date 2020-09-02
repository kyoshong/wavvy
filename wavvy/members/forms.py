from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMessage

class UserSingupForm(UserCreationForm):
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'이메일',
                'required':'True',
            }
        )
    )

    username = forms.CharField(
        required=True,
        label= False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'이름',
                'required':'True',
            }
        )
    )
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'비밀번호',
                'required':'True',
            }
        )
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'비밀번호 확인',
                'required':'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

'''
class UserSingupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'이메일',
                'required':'True',
            }
        )
    )
    username = forms.CharField(
        required=True,
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'이름',
                'required':'True',
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password',
                'required':'True',
            }
        )
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password 확인',
                'required':'True',
            }
        )
    )

    checkbox = forms.BooleanField(
        required=True,
        label='동의',
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-control',
                'required':'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','checkbox')
  '''  
class UserUpadateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']