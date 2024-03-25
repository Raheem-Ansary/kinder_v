from django.db import models



class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=4000, verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
    



class FoterGaley(models.Model):
    image = models.ImageField(upload_to='images/galeryfoter', verbose_name='تصویر فوتر')


    class Meta:
        verbose_name = 'تصویر فوتر'
        verbose_name_plural = 'گالری فوتر'



class MiddleBaner(models.Model):
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    first_image = models.ImageField(upload_to='images/middlebaner', verbose_name='تصویر اول')
    second_image = models.ImageField(upload_to='images/middlebaner', verbose_name='تصویر دوم')
    therd_image = models.ImageField(upload_to='images/middlebaner', verbose_name='تصویر سوم')

    class Meta:
        verbose_name = 'بنر وسط'
        verbose_name_plural = 'بنر های وسط'



class KindergartenClasses(models.Model):
    class_name = models.CharField(max_length=100, verbose_name='نام کلاس')
    image_class = models.ImageField(upload_to='images/classimege', verbose_name='تصویر کلاس')
    tech_name = models.CharField(max_length=200, verbose_name='نام معلم')
    tech_image = models.ImageField(upload_to='images/techimage', verbose_name='تصویر معلم')
    Childrens_age = models.CharField(max_length=10, verbose_name='سن کودکان')
    time_class = models.CharField(max_length=10, verbose_name='زمان برگذاری کلاس')
    capacity_class = models.CharField(max_length=10, verbose_name='ظرفیت کلاس')


    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'




class PopularTeachers(models.Model):
    teach_name = models.CharField(max_length=100, verbose_name='نام معلم')
    semat = models.CharField(max_length=100, verbose_name='سمت معلم')


    class Meta:
        verbose_name = 'معلم محبوب'
        verbose_name_plural = 'معلمان محبوب'