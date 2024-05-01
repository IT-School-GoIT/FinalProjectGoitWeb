from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.RegisterView.as_view(), name='signup'),
    # path('signin/',
    #      LoginView.as_view(template_name='accounts/login.html', form_class=LoginForm, redirect_authenticated_user=True),
    #      name='signin'),
    # path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('profile_settings/', views.profile_settings, name='profile_settings'),
    # path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    # path('reset-password/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>/<token>/',
    #      PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
    #                                       success_url='/accounts/reset-password/complete/'),
    #      name='password_reset_confirm'),
    # path('reset-password/complete/',
    #      PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    #      name='password_reset_complete'),
]
