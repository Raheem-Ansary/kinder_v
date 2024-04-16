from django import forms
from .models import AppointmentRequest

class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = ['guardian_name', 'guardian_phone_number', 'child_name', 'child_age', 'message']
        labels = {
            'guardian_name': 'نام والدین',
            'guardian_phone_number': 'شماره تلفن والدین',
            'child_name': 'نام فرزند',
            'child_age': 'سن فرزند',
            'message': 'پیام'
        }
