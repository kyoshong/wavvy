from django.shortcuts import render, redirect
from .forms import UserSingupForm, UserUpadateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import auth
import base64

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

def signup(request):
    if request.method == "POST":
        signup_form = UserSingupForm(request.POST)
        if signup_form.is_valid():
            user = User.objects.create_user(username=request.POST['username'], 
            password=request.POST['password1'],email=request.POST['email'])
            user.is_active = False # 유저 비활성화
            user.save()
            messages.success(request,f'your account has been created! You are now able to log in {user}!')
            message = render_to_string('logining/activation_email.html', {
                'user': user,
                'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect('signupWait')
    else:
        signup_form = UserSingupForm()
    return render(request, 'logining/signup.html', {'signup_form': signup_form})
'''
def signup(request):
    if request.method == 'POST':
        signupform = UserSingupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect(
                reverse("signup_oK")
            )
        elif request.method =='GET':
            signupform = UserSingupForm()
        return render(request, 'logining/signup.html', {
            'signup_form': signupform
            })
'''

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpadateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form' : u_form,
    'p_form' : p_form
    }

    return render(request,'mypage/profile.html', context)

def favorite(request):
    return render(request,'mypage/favorite.html')


def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # 로그인
        user = auth.authenticate(request, username=username, password=password, email=email)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        #    실  패   
        else:
            return render(request, 'logining/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'logining/login.html')

def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return redirect('index')
    return render(request, 'logining/signup.html')


def activate(request, uid64, token):
   
    uid = force_text(urlsafe_base64_decode(uid64.encode('utf-8')))
    user = User.objects.get(pk=uid)
    print(user)
   
    user.is_active = True
    user.save()
    return redirect('login')
 