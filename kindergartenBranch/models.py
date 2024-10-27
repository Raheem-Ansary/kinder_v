from django.db import models

class KindergartenBranch(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField(blank=True)  
    image = models.ImageField(upload_to="branch_images/")  
    is_featured = models.BooleanField(default=False, help_text="اگر فعال باشد، شعبه در صفحه اصلی نمایش داده می‌شود.")

    def __str__(self):
        return self.name