from django import forms
from django.core import validators
from . models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you can change password using <a href=\"../password/\">this form</a>')
    model = User
    fields = ('email', 'phone_number', 'full_name',  'password', 'last_login')



class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label="ایمیل")
    full_name = forms.CharField(label='نام و نام خوانوادگی')
    phone = forms.CharField(max_length=11, label='شماره موبایل')
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')


    def clean_email(self):
         email = self.cleaned_data['email']
         user = User.objects.filter(email=email).exists()
         if user:
            raise ValidationError('This email exists')
         return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('this phone is allredy exists.')
        return phone

          
    


class LoginForm(forms.Form):
    phone_number = forms.EmailField(
        label='شماره موبایل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(11),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(label="")
