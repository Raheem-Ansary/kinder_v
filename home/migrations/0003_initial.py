# Generated by Django 5.0.2 on 2024-04-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_phone_number', models.CharField(max_length=11)),
                ('child_name', models.CharField(max_length=100)),
                ('child_age', models.IntegerField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'درخواست وقت ملاقات',
                'verbose_name_plural': 'وقت های ملاقات',
            },
        ),
    ]