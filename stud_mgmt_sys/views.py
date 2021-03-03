from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, CreateView, DeleteView, DetailView, UpdateView
from django import views

from stud_mgmt_sys.form import LoginForm, UserModelForm
from stud_mgmt_sys.models import *


class sample_views(views.View):
     def get(self, request):
          login_form = LoginForm()
          return render(request, "index.html", {'loginform': login_form})

     def post(self, request):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username, password=password)
          if user is None:
               return redirect('home')
          else:
               if user.is_active:
                    login(request, user=user)
                    return redirect('sms:list_student')

               else:
                    return redirect('home')


class StudentListView(ListView):
     model = Students
     template_name = 'sms/list_student.html'
     context_object_name = 'students'

class StudentAddView(LoginRequiredMixin, CreateView):
     login_url = reverse_lazy('sms:login_user')
     model = Students
     template_name = 'sms/add_student.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_student')

class StudentEditView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('sms:login_user')
    model = Students
    fields = '__all__'
    template_name = 'sms/edit_student.html'
    success_url = reverse_lazy('sms:list_student')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
     login_url = reverse_lazy('sms:login_user')
     model = Students
     fields =  '__all__'
     template_name = 'sms/delete_student.html'
     success_url = reverse_lazy('sms:list_student')
     context_object_name = 'student'


class StudentDetailsView(LoginRequiredMixin, DetailView):
      login_url = reverse_lazy('sms:login_user')
      model = Students
      template_name = 'sms/details_students.html'
      context_object_name = 'student'

class StaffListView(ListView):
     model = Staffs
     template_name = 'sms/list_staff.html'
     context_object_name = 'staffs'

class StaffAddView(CreateView):
     model = Staffs
     template_name = 'sms/add_staff.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_staff')

class SubjectListView(ListView):
     model = Subject
     template_name = 'sms/list_subject.html'
     context_object_name = 'subjects'

class SubjectAddView(CreateView):
     model = Subject
     template_name = 'sms/add_subject.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_subject')



class SupervisorListView(LoginRequiredMixin, ListView):
     login_url = reverse_lazy('sms:login_user')
     model = Supervisor
     template_name = 'sms/list_supervisor.html'
     context_object_name = 'supervisors'

class SupervisorAddView(LoginRequiredMixin, CreateView):
     login_url = reverse_lazy('sms:login_user')
     model = Supervisor
     template_name = 'sms/add_supervisor.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_supervisor')

class SupervisorEditView(LoginRequiredMixin, UpdateView):
     login_url = reverse_lazy('sms:login_user')
     model = Supervisor
     template_name = 'sms/edit_supervisor.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_supervisor')

class SupervisorDeleteView(LoginRequiredMixin, DeleteView):
     login_url = reverse_lazy('sms:login_user')
     model = Supervisor
     template_name = 'sms/delete_supervisor.html'
     context_object_name = 'supervisor'
     success_url = reverse_lazy('sms:list_supervisor')

class SupervisorDetailsView(LoginRequiredMixin, DetailView):
     login_url = reverse_lazy('sms:login_user')
     model = Supervisor
     template_name = 'sms/details_supervisor.html'
     context_object_name = 'supervisor'



class FacultyListView(ListView):
     model = Faculty
     template_name = 'sms/list_faculty.html'
     context_object_name = 'faculties'

class FacultyAddView(LoginRequiredMixin, CreateView):
     login_url = reverse_lazy('sms:login_user')
     model = Faculty
     template_name = 'sms/add_faculty.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_faculty')

class FacultyEditView(LoginRequiredMixin, UpdateView):
     login_url = reverse_lazy('sms:login_user')
     model = Faculty
     template_name = 'sms/edit_faculty.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_faculty')

class FacultydeleteView(LoginRequiredMixin, DeleteView):
     login_url = reverse_lazy('sms:login_user')
     model = Faculty
     template_name = 'sms/delete_faculty.html'
     context_object_name = 'faculty'
     success_url = reverse_lazy('sms:list_faculty')

class FacultyDetailsView(DetailView):
     model = Faculty
     template_name = 'sms/details_faculty.html'
     context_object_name = 'faculty'





class BatchListView(ListView):
     model = Batch
     template_name = 'sms/list_batch.html'
     context_object_name = 'batches'

class BatchAddView(LoginRequiredMixin, CreateView):
     login_url = reverse_lazy('sms:login_user')
     model = Batch
     fields = '__all__'
     template_name = 'sms/add_batch.html'
     success_url = reverse_lazy('sms:list_batch')

class BatchEditView(LoginRequiredMixin, UpdateView):
     login_url = reverse_lazy('sms:login_user')
     model = Batch
     fields = '__all__'
     template_name = 'sms/edit_batch.html'
     success_url = reverse_lazy('sms:list_batch')

class BatchDeleteView(LoginRequiredMixin, DeleteView):
     login_url = reverse_lazy('sms:login_user')
     model = Batch
     template_name = 'sms/delete_batch.html'
     context_object_name = 'batches'
     success_url = reverse_lazy('sms:list_batch')

class SemestersListView(ListView):
     model =  Semesters
     template_name = 'sms/list_semester.html'
     context_object_name = 'semesters'

class SemestersAddView(CreateView):
     model = Semesters
     template_name = 'sms/add_semester.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_semester')


class SectionListView(LoginRequiredMixin, ListView):
     login_url = reverse_lazy('sms:login_user')
     model = Section
     template_name = 'sms/list_section.html'
     context_object_name = 'sections'

class SectionAddView(LoginRequiredMixin, CreateView):
     login_url = reverse_lazy('sms:login_user')
     model = Section
     fields = '__all__'
     template_name = 'sms/add_section.html'
     success_url = reverse_lazy('sms:list_section')

class SectioneditView(LoginRequiredMixin, UpdateView):
     login_url = reverse_lazy('sms:login_user')
     model = Section
     fields = '__all__'
     template_name = 'sms/edit_section.html'
     success_url = reverse_lazy('sms:list_section')

class SectionDeleteView(LoginRequiredMixin, DeleteView):
     login_url = reverse_lazy('sms:login_user')
     model = Section
     template_name = 'sms/delete_section.html'
     success_url = reverse_lazy('sms:list_section')
     context_object_name = 'section'

class AttendanceListView(ListView):
     model = Attendance_table
     template_name = 'sms/list_attendance.html'
     context_object_name = 'attendances'

class AttendanceAddView(CreateView):
     model = Attendance_table
     fields = '__all__'
     template_name = 'sms/add_attendance.html'
     success_url = reverse_lazy('sms:list_attendance')

class AttendanceReportListView(ListView):
     model = Attendance_Report
     template_name= 'sms/list_attendancereport.html'
     context_object_name = 'attendancereports'

class AttendanceReportAddView(CreateView):
     model = Attendance_Report
     template_name = 'sms/add_attendancereport.html'
     fields = '__all__'
     success_url = reverse_lazy('sms:list_attendancereport')


class LoginUserView(views.View):
     def get(self, request):
          loginform = LoginForm()
          return render(request, 'sms/login.html', {'loginform': loginform})

     def post(self, request):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username, password = password)
          if user is None:
               return redirect('sms:login_user')
          else:
               if user.is_active:
                    login(request, user=user)
                    return redirect('sms:list_student')
               else:
                    return redirect('sms:login_user')

class LogOutUserView(views.View):
     def get(self, request):
          logout(request)
          return redirect('home')

class RegisterUserView(views.View):
     def get(self, request):
          user_form = UserModelForm()
          return render(request, 'sms/register.html', {'form' : user_form})
     def post(self, request):
          user_form = UserModelForm(request.POST)
          if user_form.is_valid():
               user = user_form.save()
               user.set_password(user.password)
               user.save()
               login(request, user)
               return redirect('sms:list_student')
          else:
               return render(request, 'sms/register.html', {'form' : user_form})












