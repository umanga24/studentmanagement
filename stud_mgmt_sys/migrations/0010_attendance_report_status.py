# Generated by Django 3.1.1 on 2020-10-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_mgmt_sys', '0009_auto_20201014_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_report',
            name='status',
            field=models.CharField(choices=[('absent', 'absent'), ('present', 'present'), ('pending', 'pending')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
