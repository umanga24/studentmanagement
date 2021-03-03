# Generated by Django 3.1.1 on 2020-10-14 08:04

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_mgmt_sys', '0008_auto_20201011_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('student_name', models.ManyToManyField(to='stud_mgmt_sys.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.faculty')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('attendance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.attendance_table')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.students')),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_mgmt_sys.semesters'),
        ),
    ]
