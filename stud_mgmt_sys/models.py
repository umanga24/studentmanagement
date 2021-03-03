from django.db import models
from phone_field import PhoneField
from datetime import datetime



class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICE = [(GENDER_MALE, 'male'), (GENDER_FEMALE, 'female')]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    address =  models.CharField(max_length=100)
    supervisor_photo = models.ImageField(upload_to='supervisors_photo', null=True)


    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.OneToOneField(Supervisor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




class Batch(models.Model):
    batch = models.CharField(max_length=100)
    def __str__(self):
        return self.batch



class Section(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Semesters(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = PhoneField(blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    student_photo = models.ImageField(upload_to='students_photo', null=True)
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICE = [(GENDER_MALE, 'male'),(GENDER_FEMALE, 'female')]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Staffs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = PhoneField(blank=True)
    address = models.CharField(max_length=100)
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICE = [(GENDER_MALE, 'male'), (GENDER_FEMALE, 'female')]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    student_name = models.ManyToManyField(Students)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name






class Attendance_table(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    day = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.day

class Attendance_Report(models.Model):
    attendance = models.ForeignKey(Attendance_table, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True)
    STATUS_ABSENT = 'absent'
    STATUS_PRESENT = 'present'

    STATUS_CHOICE = [(STATUS_ABSENT, 'absent'), (STATUS_PRESENT, 'present')]
    status = models.CharField(max_length=100, choices=STATUS_CHOICE)

    # def __str__(self):
    #     return self.status
















