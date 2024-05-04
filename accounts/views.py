from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.

# class RegisterView(View):
#     template_name = 'accounts/register.html'
#     form_class = RegisterForm
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(to='home:home')
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         return render(request, self.template_name, context={
#             'form': self.form_class,
#             'title': 'Registration',
#         })
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             messages.success(request, f'Вітаємо {username}! Ваш акаунт успішно створено.')
#             return redirect(to='accounts:signin')
#         return render(request, self.template_name, context={'form': form})
#
#
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html', {
#         'title': 'profile',
#         'page': 'profile',
#         'app': 'accounts'
#     })
#
# @login_required
# def profile_settings(request):
#     return render(request, 'accounts/profile_settings.html', {
#         'title': 'profile_settings',
#         'page': 'profile_settings',
#         'app': 'accounts'
#     })
#
#
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'accounts/password_reset.html'
#     email_template_name = 'accounts/password_reset_email.html'
#     html_email_template_name = 'accounts/password_reset_email.html'
#     success_url = reverse_lazy('accounts:password_reset_done')
#     success_message = "An email with instructions to reset your password has been sent to %(email)s."
#     subject_template_name = 'accounts/password_reset_subject.txt'
