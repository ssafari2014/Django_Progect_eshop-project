from django.contrib.auth import login, logout
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import registerForm, loginForm, ForgotForm, ResetForm
from .models import User
from utils.email_service import send_email


# Create your views here.

class register_View(View):
    def get(self, request):
        register_forms = registerForm()
        return render(request, 'account_module/register.html', context={
            'register_forms': register_forms
        })

    def post(self, request: HttpRequest):
        register_forms = registerForm(request.POST)
        if register_forms.is_valid():
            user_email = register_forms.cleaned_data.get('email')
            user_pass = register_forms.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_forms.add_error('email', error='با اطلاعات وارد شده شخص دیگری وارد کرده ')
                return redirect(reverse('login-page'))
            new_user = User(
                username=user_email,
                email_active_code=get_random_string(72),
                email=user_email,
                is_active=False,
            )
            new_user.set_password(user_pass)
            new_user.save()
            # send email user is_activate account redirect login page
            send_email('ایمیل فعالسازی حساب کاربری',
                       to=new_user.email,
                       context={'user': new_user},
                       template_name='emails/active_account.html'
                       )
            return redirect(reverse('index-page'))

        return render(request, 'account_module/register.html', context={
            'register_forms': register_forms
        })


class Login_View(View):
    def get(self, request):
        login_forms = loginForm()
        return render(request, 'account_module/login.html', context={
            'login_forms': login_forms
        })

    def post(self, request: HttpRequest):
        login_forms = loginForm(request.POST)
        if login_forms.is_valid():
            user_email = login_forms.cleaned_data.get('email')
            user_pass = login_forms.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    check_password = user.check_password(user_pass)
                    if check_password:
                        login(request, user)
                        return redirect(reverse('index-page'))
                    login_forms.add_error('email', 'اطلاعات وارد شده مغایرتی دارد مجدد اقدام نمایید ')
                login_forms.add_error('email', 'حساب کاربری شما تا کنون فعال نشده است!')
            login_forms.add_error('email', 'با اطلاعات فوق تا کنون ثبت نامی انجام نشده است! ')

        return render(request, 'account_module/login.html', context={
            'login_forms': login_forms
        })


class Active_Account_View(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login-page'))

        # show error redirect register
        raise Http404


class Forgot_Password_View(View):
    def get(self, request):
        forgot_forms = ForgotForm()
        return render(request, 'account_module/forgot.html', context={
            'forgot_forms': forgot_forms
        })

    def post(self, request: HttpRequest):
        forgot_forms = ForgotForm(request.POST)
        if forgot_forms.is_valid():
            user_email = forgot_forms.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # send email redirect home
                send_email('بازیابی گذرواژه',
                           to=user.email,
                           context={'user': user},
                           template_name='emails/forgot_password.html'
                           )
            forgot_forms.add_error('email', 'کاربری با اطلاعات فوق وجود ندارد !')
        return render(request, 'account_module/forgot.html', context={
            'forgot_forms': forgot_forms
        })


class Reset_Password_View(View):
    def get(self, request: HttpRequest, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            reset_pass = ResetForm()
            return render(request, 'account_module/reset.html', context={
                'reset_pass': reset_pass,
                'user': user,
            })
        return redirect(reverse('login-page'))

    def post(self, request: HttpRequest, email_active_code):
        reset_pass = ResetForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if reset_pass.is_valid():
            if user is not None:
                user_pass = reset_pass.cleaned_data.get('password')
                user.set_password(user_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login-page'))
            return redirect(reverse('login-page'))
        return render(request, 'account_module/reset.html', context={
            'reset_pass': reset_pass,
            'user': user,
        })


class Logout_View(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
