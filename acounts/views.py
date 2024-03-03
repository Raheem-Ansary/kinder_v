from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest
from . forms import LoginForm, UserRegistrationForm, VerifyCodeForm
from django.views import View
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth import login, logout
import random
from utils.send_otp_code import send_code





class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_code(form.cleaned_data['phone'], form.cleaned_data['full_name'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }

        
            messages.success(request, 'برای شما کد ارسال شد', 'success')
            return redirect('accounts:verify_code')
        
            messages.error(request, 'this code is wrang', 'danger')
        return render(request, self.template_name, {'form': form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], 
                                         user_session['full_name'], user_session['password'])
                code_instance.delete()
               
                messages.success(request, 'ثبت نام باموفقیت انجام شد', 'success')
                return redirect( 'accounts:login_page')
            else:
                messages.error(request, 'کد وارد شده اشتباه است', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home_page:home_page')


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'accounts/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('phone_number')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page:home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'accounts/login.html', context)
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('accounts:login_page'))


def Profile(request: HttpRequest):
    return render(request, 'user_panel_module/user_panel_dashboard_page.html')



