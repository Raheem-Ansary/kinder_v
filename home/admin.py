from django.contrib import admin
from .models import AppointmentRequest

class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('guardian_name', 'guardian_phone_number', 'child_name', 'child_age', 'created_at')
    search_fields = ('guardian_name', 'guardian_phone_number', 'child_name')  
    list_filter = ('created_at',)  
    readonly_fields = ['guardian_name', 'guardian_phone_number', 'child_name', 'child_age', 'message']

admin.site.register(AppointmentRequest, AppointmentRequestAdmin)
