from django.db import models




class AppointmentRequest(models.Model):
    guardian_name = models.CharField(verbose_name = 'نام والدین', max_length=100)
    guardian_phone_number = models.CharField(verbose_name= 'شماره موبایل والدین', max_length=11)
    child_name = models.CharField(verbose_name= 'نام فرزند',max_length=100)
    child_age = models.IntegerField(verbose_name='سن کودک')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(verbose_name='تاریخ ثبت', auto_now_add=True)

    def __str__(self):
        return f"Appointment Request from {self.guardian_name}"

    class Meta:
        verbose_name = 'درخواست وقت ملاقات'
        verbose_name_plural = 'وقت های ملاقات'