# Generated by Django 5.0.2 on 2024-03-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoterGaley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/galeryfoter', verbose_name='تصویر فوتر')),
            ],
            options={
                'verbose_name': 'تصویر فوتر',
                'verbose_name_plural': 'گالری فوتر',
            },
        ),
        migrations.CreateModel(
            name='KindergartenClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, verbose_name='نام کلاس')),
                ('image_title', models.ImageField(upload_to='images/classimege')),
                ('tech_name', models.CharField(max_length=200, verbose_name='نام معلم')),
                ('tech_image', models.ImageField(upload_to='images/techimage', verbose_name='تصویر معلم')),
                ('Childrens_age', models.CharField(max_length=10, verbose_name='سن کودکان')),
                ('time_class', models.CharField(max_length=10, verbose_name='زمان برگذاری کلاس')),
                ('capacity_class', models.CharField(max_length=10, verbose_name='ظرفیت کلاس')),
            ],
            options={
                'verbose_name': 'کلاس',
                'verbose_name_plural': 'کلاس ها',
            },
        ),
        migrations.CreateModel(
            name='MiddleBaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/middlebaner', verbose_name='تصویر میانی')),
            ],
            options={
                'verbose_name': 'بنر وسط',
                'verbose_name_plural': 'بنر های وسط',
            },
        ),
        migrations.CreateModel(
            name='PopularTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_name', models.CharField(max_length=100, verbose_name='نام معلم')),
                ('semat', models.CharField(max_length=100, verbose_name='سمت معلم')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.CharField(max_length=4000, verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
