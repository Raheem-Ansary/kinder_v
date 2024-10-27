from django.contrib import admin

from . import models


admin.site.register(models.Slider)
admin.site.register(models.KindergartenClasses)
admin.site.register(models.PopularTeachers)
admin.site.register(models.MiddleBaner)

@admin.register(models.MiniGallery)
class MiniGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


