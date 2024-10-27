from django.contrib import admin
from .models import KindergartenArticle

@admin.register(KindergartenArticle)
class KindergartenArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
