# Generated by Django 3.1.1 on 2020-10-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_mgmt_sys', '0005_auto_20201011_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.IntegerField(choices=[('male', 'male'), ('female', 'female')]),
        ),
    ]
