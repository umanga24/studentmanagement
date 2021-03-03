# Generated by Django 3.1.1 on 2020-10-14 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_mgmt_sys', '0010_attendance_report_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.semesters'),
        ),
    ]