# Generated by Django 3.1.1 on 2020-10-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_mgmt_sys', '0006_auto_20201011_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100),
        ),
    ]
