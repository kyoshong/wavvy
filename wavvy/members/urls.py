from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('favorite/',views.favorite, name='favorite'),
    path('profile/',views.profile, name='profile'),
    path('signup/',views.signup, name='signup'),
    path('signupWait/',auth_views.LoginView.as_view(template_name='logining/signupWait.html'), name='signupWait'),
    path('login/', auth_views.LoginView.as_view(template_name='logining/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logining/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='mypage/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='mypage/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]