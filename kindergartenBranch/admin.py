# admin.py

from django.contrib import admin
from .models import KindergartenBranch

@admin.register(KindergartenBranch)
class KindergartenBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'address')
