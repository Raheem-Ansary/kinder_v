from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget 
from .models import Category


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(config_name='default'))  

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
