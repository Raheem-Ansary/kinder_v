from django.db import models
from django_ckeditor_5.fields import CKEditor5Field 

class KindergartenArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image = models.ImageField(upload_to="article_images/", verbose_name="تصویر")
    content = CKEditor5Field(verbose_name="محتوا")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
