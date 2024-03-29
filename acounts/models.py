from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import UserManager

# Create your models here.



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=20, verbose_name='نام و نام خوانوادگی')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')
    email = models.EmailField(max_length=100, unique=True, verbose_name='ایمیل')
    is_admin = models.BooleanField(default=False, verbose_name='حالت ادمین')

    objects = UserManager()

    class Meta:
        verbose_name = 'یوزر'
        verbose_name_plural = 'یوزر ها'

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    

class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'