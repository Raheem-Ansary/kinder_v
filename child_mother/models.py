from django.db import models
from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field 

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')
    description = CKEditor5Field('Description', config_name='default')  
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

